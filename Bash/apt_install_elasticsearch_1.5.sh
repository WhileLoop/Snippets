wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb http://packages.elastic.co/elasticsearch/1.5/debian stable main" | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get -y install elasticsearch openjdk-7-jre-headless
sudo update-rc.d elasticsearch defaults 95 10
