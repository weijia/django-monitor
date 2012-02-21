#!/bin/bash

cat /proc/partitions |egrep '\bsda\b' |egrep -o '\b[0-9][0-9]*[0-9]\b'
