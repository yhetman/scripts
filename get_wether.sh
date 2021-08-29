#!/bin/bash

counter=3000

while true
do
	curl "api.openweathermap.org/data/2.5/find?lat=50.27&lon=30.31&cnt=20&appid=e249f6c962e15ea4c8f64c40f78bb7dc" > weather$counter.json
	sleep 60
	counter=$((counter - 1))
	if [[ $counter -lt 0 ]] ; then
		break ;
	fi
done

