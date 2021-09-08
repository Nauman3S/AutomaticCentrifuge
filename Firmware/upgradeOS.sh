#!/bin/sh
sudo apt update && sudo upgrade -y
if [ $? -eq 0 ]; then
   echo OK>/home/pi/AutoCentrifuge/logs/upgradeOP.txt
else
   echo FAIL>/home/pi/AutoCentrifuge/logs/upgradeOP.txt
fi
