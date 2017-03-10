#!/bin/bash

# Get interface name from parameters
if [ $# -eq 0 ]
then
        iface="eth0"
else
        iface="$1"
fi

cmd=$(ifconfig $iface | grep 'inet' | awk '{ print $2 }')
python /home/spondbob/projects/tweety/tweety.py "Say hello to $cmd"
