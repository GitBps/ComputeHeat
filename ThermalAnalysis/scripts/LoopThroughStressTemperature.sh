#!/bin/bash

# Get the PID of the process
pid=$(pidof -d sep  $1)

if [ -z "$pid" ]; then
    echo "Process not found"
    exit 1
fi

echo  $pid

# Set the delimiter
delimiter="s"

individualPIDs=$(echo $pid | tr "s" "\n")



for addr in $individualPIDs
do
	#commandToExecute="sudo taskset -pc "$2" "$addr""
	commandToExecute="python3 runtimeAnalyzer.py FilteredCPU0 "$addr" 6" 
	echo "$addr" $commandToExecute
	# Pass the parameters to another script
	$commandToExecute
	sleep 1
done



