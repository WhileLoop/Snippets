import boto.cloudformation
import time

stack_name = ""
ami_id = ""
template_filename = ""
verbose = False;

params = [('AmiParam', ami_id)]
tags = {'stack' : stack_name}

# Read template.
with open (template_filename, "r") as template_file:
    template_data = template_file.read()

# Create stack.
conn = boto.cloudformation.connection.CloudFormationConnection()
conn.create_stack(stack_name, template_body = template_data, parameters = cf_params, tags = cf_tags)

# Poll for creation.
dns = ""
should_loop = True
while should_loop: # FIXME: Add timeout.
  for stack in conn.describe_stacks(stack_name_or_id=cf_stack_name):
    if (stack.stack_name == cf_stack_name):
      if (stack.stack_status == 'CREATE_COMPLETE'):
        should_loop = False;
        break;
  time.sleep(5);
