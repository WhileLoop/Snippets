wget -q -O- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | sudo apt-key add -
echo "deb https://deb.nodesource.com/node_0.12 trusty main" | sudo tee -a /etc/apt/sources.list.d/nodesource.list
echo "deb-src https://deb.nodesource.com/node_0.12 trusty main" | sudo tee -a /etc/apt/sources.list.d/nodesource.list
sudo apt-get update
sudo apt-get install -y nodejs
