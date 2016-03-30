echo "deb http://toolbelt.heroku.com/ubuntu ./" > /etc/apt/sources.list.d/heroku.list
wget -O- https://toolbelt.heroku.com/apt/release.key | apt-key add -
apt-get update
apt-get install -y ruby heroku-toolbelt
