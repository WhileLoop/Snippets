sudo add-apt-repository "deb http://apt.nuxeo.org/ trusty releases"
wget -q -O- http://apt.nuxeo.org/nuxeo.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y nuxeo
