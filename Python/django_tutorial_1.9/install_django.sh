#!/bin/sh

sudo apt-get update
sudo apt-get install python-pip python-dev -y
sudo -H pip install --upgrade pip
sudo -H pip install django==1.9.1
sudo -H pip install Pillow==2.9.0
