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


## Setup the Stressing utility for simulating the heat and temperature due to heat. 

sudo ./ThermalAnalysis/tools/stress-ng --matrix 35  --timeout 15m --thermalstat 1

This will do a 35 instances of matrix multiplications and enough to load the 12 CPUs in this case 

Sample output shall provide following columns 

  |stress-ng: info:  [23205] setting to a 15 mins, 0 secs run per stressor                                                             |
  |------------------------------------------------------------------------------------------------------------------------------------|
  |stress-ng: info:  [23205] dispatching hogs: 35 matrix                                                                               |
  |stress-ng: info:  [23206] therm: AvGHz MnGHz MxGHz  LdA1  LdA5 LdA15    AMBF INT340   NGFF   TCPU TCPU_P   TMEM   TSKN iwlwif x86_pk|
  |stress-ng: info:  [23206] therm:  3.53  3.20  4.18  3.16  1.00  0.69   34.05  20.00  48.05  87.05  93.00  46.05  50.05  45.00  92.00|
  |stress-ng: info:  [23206] therm:  3.35  3.05  3.95  3.16  1.00  0.69   34.05  20.00  48.05  91.05  92.00  47.05  51.05  46.00  92.00|
  |stress-ng: info:  [23206] therm:  3.42  3.12  4.02  3.16  1.00  0.69   34.05  20.00  48.05  91.05  91.00  47.05  55.05  45.00  92.00|
  |stress-ng: info:  [23206] therm:  3.41  3.12  4.00  3.16  1.00  0.69   34.05  20.00  48.05  91.05  92.00  47.05  55.05  45.00  91.00|
  |stress-ng: info:  [23206] therm:  3.33  3.05  3.87  3.16  1.00  0.69   34.05  20.00  48.05  91.05  92.00  47.05  57.05  45.00  92.00|
  |stress-ng: info:  [23206] therm:  3.27  3.00  3.80  5.71  1.57  0.87   34.05  20.00  48.05  91.05  91.00  47.05  58.05  45.00  92.00|
  |stress-ng: info:  [23206] therm:  3.26  3.00  3.79  5.71  1.57  0.87   34.05  20.00  48.05  91.05  91.00  47.05  59.05  45.00  91.00|
  |stress-ng: info:  [23206] therm:  3.25  3.00  3.75  5.71  1.57  0.87   34.05  20.00  48.05  91.05  91.00  47.05  61.05  45.00  91.00|
  |------------------------------------------------------------------------------------------------------------------------------------|
  

## Kernel Code Changes for Diagnostics 

In the linux kernel 6.6.8, we modified and put diagnostics to read the temperature from the hardwrae insitu. 

This is then later plotted using the python analyzers for this research work. 

Ideally it should be a part of the temperature schedulers to control internally itself. 

![image](https://github.com/GitBps/ComputeHeat/assets/47725750/c5bcab0e-e218-411b-b826-1c9aed6d9471)

Instruments are present in the following files 

![image](https://github.com/GitBps/ComputeHeat/assets/47725750/ff9aaf44-c0b3-433b-bbb3-e5ca6b292538)


## Diagnostics and Analytics of thermal material 

|Collection Scripts |
|------------------------------------------------------------------------------------------------------------------------------------|
|sudo trace-cmd report --cpu 0 /root/trace_event_logging_iter3.dat > CPU0.txt|
|sudo trace-cmd report --cpu 1 /root/trace_event_logging_iter3.dat > CPU1.txt|
|sudo trace-cmd report --cpu 2 /root/trace_event_logging_iter3.dat > CPU2.txt|
|sudo trace-cmd report --cpu 3 /root/trace_event_logging_iter3.dat > CPU3.txt|
|sudo trace-cmd report --cpu 4 /root/trace_event_logging_iter3.dat > CPU4.txt|
|sudo trace-cmd report --cpu 5 /root/trace_event_logging_iter3.dat > CPU5.txt|
|sudo trace-cmd report --cpu 6 /root/trace_event_logging_iter3.dat > CPU6.txt|
|sudo trace-cmd report --cpu 7 /root/trace_event_logging_iter3.dat > CPU7.txt|
|cat CPU0.txt | grep -iP ".*000.*sched_stat_runtime.*stress|.*000.*Balv" CPU0.txt > FilteredCPU00.txt|
|cat CPU1.txt | grep -iP ".*001.*sched_stat_runtime.*stress|.*001.*Balv" CPU1.txt > FilteredCPU01.txt|
|cat CPU2.txt | grep -iP ".*002.*sched_stat_runtime.*stress|.*002.*Balv" CPU2.txt > FilteredCPU02.txt|
|cat CPU3.txt | grep -iP ".*003.*sched_stat_runtime.*stress|.*003.*Balv" CPU3.txt > FilteredCPU03.txt|
|cat CPU4.txt | grep -iP ".*004.*sched_stat_runtime.*stress|.*004.*Balv" CPU4.txt > FilteredCPU04.txt|
|cat CPU5.txt | grep -iP ".*005.*sched_stat_runtime.*stress|.*005.*Balv" CPU5.txt > FilteredCPU05.txt|
|cat CPU6.txt | grep -iP ".*006.*sched_stat_runtime.*stress|.*006.*Balv" CPU6.txt > FilteredCPU06.txt|
|cat CPU7.txt | grep -iP ".*007.*sched_stat_runtime.*stress|.*007.*Balv" CPU7.txt > FilteredCPU07.txt|
|------------------------------------------------------------------------------------------------------------------------------------|

Now to generate Graphs and Quadratic Fit for all the processes you can use the following commands

python3 runtimeAnalyzer.py FilteredCPU0 <pid> 1

python3 ../runtimeAnalyzer.py FilteredCPU0 <pid> 1




