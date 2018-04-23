#!/bin/sh
# launch2.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/Desktop/RASPBERRY_ANTIFIRE/dhtWebSensor
python3 Sensordata.py
cd /

