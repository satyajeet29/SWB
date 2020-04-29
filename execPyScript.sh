#!/bin/bash
echo "$(date '+%Y %b %d %H:%M:%S'):: Started";
c=0
s=0
f=0
while true
do
    ((c=c+1))
    echo "--->> $(date '+%Y %b %d %H:%M:%S') :: Sequence $c "
    (command python3 TwitterCursorSet0.py && ((s = s+1)) && echo "Success #: $s") || (((f=f+1))&& echo "Failure #: $f")
    echo "Sleeping now for 45 minutes"
    sleep 45m
done