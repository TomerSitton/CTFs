#!/bin/bash
echo "Content-type: text/html"
echo ""
echo ""
echo "MORTY'S MACHINE TRACER MACHINE"
echo "
Enter an IP address to trace.
"
echo "
"
echo ""
echo ""
echo ""
echo "
"

OIFS="$IFS"

IFS="${IFS}&"
set $QUERY_STRING > /dev/null
args="$*"
IFS="$OIFS"
IP=""

echo "OIFS:" $OIFS
echo "IFS:" $IFS
echo "args:" $args
echo "QUERY STRING:" $QUERY_STRING
QUERY_STRING=$args
echo "args:" $args
echo "QUERY STRING:" $QUERY_STRING

if [ -z "$QUERY_STRING" ]; then
    echo "EXIT!"
    exit 0
fi

IP=`echo "$QUERY_STRING" | sed -n 's/^.*ip=\([^&]*\).*$/\1/p' | sed "s/%3B/;/g" | sed "s/%20/ /g" | sed "s/%2F/\//g" | sed "s/\+/ /g" | sed "s/%3C/\/g"`
echo "IP:" $IP

echo "

"
eval "traceroute $IP"
echo "

"
echo ""
exit 0
