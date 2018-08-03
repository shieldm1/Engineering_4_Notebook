#!/bin/bash
# blink an led

gpio mode 0 out

for i in {1..5}
do
	gpio write 0 1
	echo $i
	sleep 1
	gpio write 0 0
	echo off
	sleep 1
done

