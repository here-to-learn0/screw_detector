#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H%M") 
fswebcam /home/pi/photos/$DATE.jpg
python exp_python.py --filename /home/pi/photos/$DATE.jpg
# scp *.jpg vardeep@192.168.0.169:/home/vardeep/Desktop/