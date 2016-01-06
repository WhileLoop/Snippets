# Usage: fab get_all_datestamps:elb_name=my_elb_name -i deployment_key.pem -f fabric_ec2_ntp_check.py --hide running,stdout -g 54.10.10.100 -u ec2-user
# Checks the system clock skew of all EC2 hosts behind a ELB load balancer. Measures the average time between all hosts and checks if any hosts is deviating.

from fabric.api import *
import boto.ec2.elb
import boto.ec2
import sys

# This executes on each host behind the load balancer. Gets the current system time and returns it.
@task
@parallel
def get_datestamp_task():
    return run('date +%s')

@task
@runs_once
def get_all_datestamps(elb_name):
    env.hosts = get_host_ips(elb_name)      # Use the AWS API to get the IP addresses of all hosts behind the ELB.
    results = execute(get_datestamp_task)   # Run the 'get_datestamp_task' task on each host. Returns a dict of epoch timestamps.
    # The timestamp of all hosts are added together and then divided by the number of hosts to get an average.
    # The timestamp of each individual host is then comapred to the average to check if deviation is outside of acceptable range.
    average = 0
    for key, value in results.iteritems() :
        average = average + int(value)
    average = average / len(results)
    print "Average timestamp is ", average
    threshold = 3   # Define maximum deviance.
    failed = False  # Need to know if any hosts failed.
    # Make sure each result is within threshold.
    for key, value in results.iteritems() :
        if int(value) + threshold < average or int(value) - threshold > average :
            print "Time in host " + key + " is off! " + value
            failed = True
        else :
            print "Host " + key + " is ok " + value
    # If any host failed return with exit code 1. Used by Jenkins to mark job failed.
    if failed:
        sys.exit(1)

def get_host_ips(elb_name):
    elb_conn = boto.ec2.elb.ELBConnection()
    # Get load balancer by name. Should only return one, but may return more than one if similar load balancer names exists. TODO: Assert name matches.
    load_balancers = elb_conn.get_all_load_balancers(elb_name)
    target_elb = load_balancers[0] # Assume first one is the one we want.
    ec2_instance_ids = [ec2_info.id for ec2_info in target_elb.instances] # Get a list of all instance ids registered to the load balancer.
    # Use the instance ids to get the private ip of the instances.
    ec2_conn = boto.ec2.connect_to_region("us-east-1")
    ec2_instances = ec2_conn.get_only_instances(instance_ids=ec2_instance_ids)
    instance_private_ips = [ec2_instance.private_ip_address for ec2_instance in ec2_instances]
    return instance_private_ips
