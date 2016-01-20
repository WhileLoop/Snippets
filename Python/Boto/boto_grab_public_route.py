# Execute on a EC2 instance to make that instance 'grab' the public route in a predetermined route table.
import boto
import boto.utils

route_table_id = ''
instance_id = boto.utils.get_instance_metadata()['instance-id']

vpc_conn = boto.connect_vpc()
rt = vpc_conn.get_all_route_tables(route_table_ids=route_table_id)[0]
vpc_conn.replace_route(rt.id, '0.0.0.0/0', instance_id=instance_id)
