#!/bin/bash
echo "$(date '+%Y %b %d %H:%M:%S'):: Started";
c = 0
s = 0
f =0
while true
do
    echo "--->> $(date '+%Y %b %d %H:%M:%S') :: Sequence $c "
    (command python3 twitterCursorDC.py && ((s = s+1)) && echo "Success #: $s") || (((f=f+1))&& echo "Failure #: $f" && continue)
    echo "Sleeping now for 45 minutes"
    sleep 45m
done