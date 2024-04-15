#!/bin/bash

SelectCPUFreqDriver=$2
SelectGovernor=$1 

echo "Start value"
sudo cat  /sys/devices/system/cpu/cpu0/cpufreq/scaling_driver 
sudo cat  /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu2/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu3/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu5/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu6/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu7/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu8/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu9/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu10/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu11/cpufreq/scaling_governor 

sudo echo "$2" >  /sys/devices/system/cpu/cpu0/cpufreq/scaling_driver 
sudo echo "$1" >  /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor 
sudo echo "$1" >  /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor 
sudo echo "$1" >  /sys/devices/system/cpu/cpu2/cpufreq/scaling_governor 
sudo echo "$1" >  /sys/devices/system/cpu/cpu3/cpufreq/scaling_governor 
sudo echo "$1" >  /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor 
sudo echo "$1" >  /sys/devices/system/cpu/cpu5/cpufreq/scaling_governor 
sudo echo "$1" >  /sys/devices/system/cpu/cpu6/cpufreq/scaling_governor 
sudo echo "$1" >  /sys/devices/system/cpu/cpu7/cpufreq/scaling_governor 
sudo echo "$1" >  /sys/devices/system/cpu/cpu8/cpufreq/scaling_governor 
sudo echo "$1" >  /sys/devices/system/cpu/cpu9/cpufreq/scaling_governor 
sudo echo "$1" >  /sys/devices/system/cpu/cpu10/cpufreq/scaling_governor 
sudo echo "$1" >  /sys/devices/system/cpu/cpu11/cpufreq/scaling_governor 

echo "Changed value"
sudo cat  /sys/devices/system/cpu/cpu0/cpufreq/scaling_driver 
sudo cat  /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu2/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu3/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu5/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu6/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu7/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu8/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu9/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu10/cpufreq/scaling_governor 
sudo cat  /sys/devices/system/cpu/cpu11/cpufreq/scaling_governor 
