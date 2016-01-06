# Usage: python boto-get-rds-logs us-east-1 dr16eb76m902o1j 1452104128607

import sys
import boto.rds

boto_rds_region = sys.argv[1]
boto_rds_dbname = sys.argv[2]
logs_start_time = sys.argv[3] # POSIX timestamp in miliseconds.

conn = boto.rds.connect_to_region(boto_rds_region)
# Get a list of log files.
rds_logs = conn.get_all_logs(boto_rds_dbname, file_last_written=logs_start_time)
for log in rds_logs:
  log_file = conn.get_log_file(boto_rds_dbname, log) # Download each log file.
  log_filename = log_file.log_filename.log_filename  # Get the log filename.
  log_filename = log_filename.replace('error/', '')  # Remove 'error/'' from filename.
  # Write the contents to disk.
  f = open(log_filename, 'w+')
  f.write(log_file.data);
  f.close()
