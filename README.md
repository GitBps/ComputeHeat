# Analyzing the Heat And Temperature Gradient during Computations 

Various Openly available (Non-commercial) Linux based tools/diagnostics for Thermal Analytics.

## CPUFrequency Governor 

For the thermal analysis since most of the tasks are CFS based. These tasks also need to be able to control per entry and per exit of the tasks from the Runqueues. Hence we have selected the SCHEDUTIL based governor.

Incase of Intel Processors used, first disable the intel-pstate driver and select the SCHEDUTIL as CPUFREQ Governor by following the below steps


## Disable the Intel-pstate

sudo nano /etc/default/grub

## Add the below line to disable the pstate at runtime in the kernel

GRUB_CMDLINE_LINUX_DEFAULT="quiet splash **intel_pstate=disable**"

sudo update-grub

sudo reboot

## Now we will select the SCHEDUTIL Governor

sudo su -l

./ThermalAnalysis/scripts/SetGovernorPolicy.sh schedutil

## Setup the S-TUI now for visually monitoring the Temperature, Per core frequency, Fanspeed, Wattage and CPU Utilization per core 

sudo s-tui 

Sample output shall look like this: 

![image](https://github.com/GitBps/ComputeHeat/assets/47725750/c3b5640f-7fdc-4727-9534-3682e52a127f)


## Setup the S-TUI now for visually monitoring the Temperature, Per core frequency, Fanspeed, Wattage and CPU Utilization per core 

sudo ./ThermalAnalysis/tools/stress-ng --matrix 35  --timeout 15m --thermalstat 1

This will do a 35 instances of matrix multiplications and enough to load the 12 CPUs in this case 

Sample output shall provide following columns 

  stress-ng: info:  [23205] setting to a 15 mins, 0 secs run per stressor
  
  stress-ng: info:  [23205] dispatching hogs: 35 matrix
  
  stress-ng: info:  [23206] therm: AvGHz MnGHz MxGHz  LdA1  LdA5 LdA15    AMBF INT340   NGFF   TCPU TCPU_P   TMEM   TSKN iwlwif x86_pk
  
  stress-ng: info:  [23206] therm:  3.53  3.20  4.18  3.16  1.00  0.69   34.05  20.00  48.05  87.05  93.00  46.05  50.05  45.00  92.00
  
  stress-ng: info:  [23206] therm:  3.35  3.05  3.95  3.16  1.00  0.69   34.05  20.00  48.05  91.05  92.00  47.05  51.05  46.00  92.00
  
  stress-ng: info:  [23206] therm:  3.42  3.12  4.02  3.16  1.00  0.69   34.05  20.00  48.05  91.05  91.00  47.05  55.05  45.00  92.00
  
  stress-ng: info:  [23206] therm:  3.41  3.12  4.00  3.16  1.00  0.69   34.05  20.00  48.05  91.05  92.00  47.05  55.05  45.00  91.00
  
  stress-ng: info:  [23206] therm:  3.33  3.05  3.87  3.16  1.00  0.69   34.05  20.00  48.05  91.05  92.00  47.05  57.05  45.00  92.00
  
  stress-ng: info:  [23206] therm:  3.27  3.00  3.80  5.71  1.57  0.87   34.05  20.00  48.05  91.05  91.00  47.05  58.05  45.00  92.00
  
  stress-ng: info:  [23206] therm:  3.26  3.00  3.79  5.71  1.57  0.87   34.05  20.00  48.05  91.05  91.00  47.05  59.05  45.00  91.00
  
  stress-ng: info:  [23206] therm:  3.25  3.00  3.75  5.71  1.57  0.87   34.05  20.00  48.05  91.05  91.00  47.05  61.05  45.00  91.00










