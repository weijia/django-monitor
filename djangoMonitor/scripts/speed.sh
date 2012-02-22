#!/bin/bash

TMP1=/tmp/tmp.txt
TMP2=/tmp/rxtx.txt
INTERVAL=10

ifconfig > $TMP1
cat $TMP1 | grep "RX bytes" | awk -F: '{print $2}' | awk '{print $1}' > $TMP2
COUNT=0
while read RX1[$[COUNT]]; do
    COUNT=$[COUNT+1]
done < $TMP2
cat $TMP1 | grep "TX bytes" | awk -F: '{print $3}' | awk '{print $1}' > $TMP2
COUNT=0
while read TX1[$[COUNT]]; do
    COUNT=$[COUNT+1]
done < $TMP2

sleep $INTERVAL

ifconfig > $TMP1
cat $TMP1 | grep "RX bytes" | awk -F: '{print $2}' | awk '{print $1}' > $TMP2
COUNT=0
while read RX2[$[COUNT]]; do
    COUNT=$[COUNT+1]
done < $TMP2
cat $TMP1 | grep "TX bytes" | awk -F: '{print $3}' | awk '{print $1}' > $TMP2
COUNT=0
while read TX2[$[COUNT]]; do
    COUNT=$[COUNT+1]
done < $TMP2

cat $TMP1 | grep "Link encap" | awk '{print $1}' > $TMP2
COUNT=0
while read IF[$[COUNT]]; do
    RX=`expr ${RX2[$[COUNT]]} - ${RX1[$[COUNT]]}`
    TX=`expr ${TX2[$[COUNT]]} - ${TX1[$[COUNT]]}`
    R0=$[$RX/$INTERVAL/1024]
    T0=$[$TX/$INTERVAL/1024]
    R1=$[$RX/$INTERVAL/102-$R0*10]
    T1=$[$TX/$INTERVAL/102-$T0*10]
    echo -e "${IF[$[COUNT]]}\t\tRX: ${R0}.${R1}KB/s\t\tTX: ${T0}.${T1}KB/s"
    COUNT=$[COUNT+1]
done < $TMP2

rm -f $TMP1 $TMP2
