wget -q -O- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
sudo sh -c 'echo deb https://deb.nodesource.com/node_0.12 trusty main' > /etc/apt/sources.list.d/nodesource.list
sudo sh -c 'echo deb-src https://deb.nodesource.com/node_0.12 trusty main' >> /etc/apt/sources.list.d/nodesource.list
sudo apt-get update
sudo apt-get install -y nodejs
