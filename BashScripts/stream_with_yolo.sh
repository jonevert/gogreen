#!/bin/bash

# In YOLO: cap = cv2.VideoCapture("tcp://127.0.0.1:9999") 

# while: keeps trying to send stream even if connection breaks.
while :; do
	echo "1280x720 $1 fsp";
	#flaggar: -n = windowless, -sh = sharpness, -hf vertical flip
	raspivid -n -vf -hf  -a 12 -t 0 -w 1280 -h 720 -hf -ih -fps $1 -l -o tcp://0.0.0.0:8160
	read -t 2 -sn 1 haltit		#attempt at a stopper
	if [[ "$haltit" = "s" ]]; then
		break
	fi
done;
