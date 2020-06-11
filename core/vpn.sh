#!/bin/bash
read -p "Enter the time(In seconds) :" t
servers=("JP" "NL" "US")
while true
do
 i=`expr $RANDOM % 3`
 protonvpn d
 protonvpn c --cc ${servers[$i]}
 echo "Sleeping for $t seconds"
 sleep $t
done 

