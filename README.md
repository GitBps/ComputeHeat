# ComputeHeat
Various Openly available (Non-commercial) Linux based tools/diagnostics for Thermal Analytics.

# CPUFrequency Governor 
For the thermal analysis since most of the tasks are CFS based. These tasks also need to be able to control per entry and per exit of the tasks from the Runqueues
Hence we have selected the SCHEDUTIL based governor.

  Incase of Intel Processors used, first disable the intel-pstate driver and select the SCHEDUTIL as CPUFREQ Governor by following the below **steps
  Disable the Intel-pstate**
  sudo nano /etc/default/grub
  **Add the below line to disable the pstate at runtime in the kernel**
  GRUB_CMDLINE_LINUX_DEFAULT="quiet splash intel_pstate=disable"
  sudo update-grub
  sudo reboot


Now we will select the SCHEDUTIL Governor
