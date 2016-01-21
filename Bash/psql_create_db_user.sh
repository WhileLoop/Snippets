sudo su postgres -c "psql <<EOF
CREATE USER db_user WITH PASSWORD 'passowrd';
CREATE DATABASE mydb WITH ENCODING 'UTF8' OWNER db_user;
EOF"
