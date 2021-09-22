#!/bin/bash

for x in {1..65}; do
	wget --timeout=1 --tries=1 10.0.2.4:$x
done
