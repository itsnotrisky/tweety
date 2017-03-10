#!/bin/bash

temp=$(/opt/vc/bin/vcgencmd measure_temp | cut -d '=' -f 2 | cut -d "'" -f 1)
python /home/spondbob/projects/tweety/tweety.py $temp"C. I'm hot."
