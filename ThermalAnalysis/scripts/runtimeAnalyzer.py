import struct
import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#from matplotlib.animation import FuncAnimation
import numpy as np
import random
import time
import sys


# Initializing the lists
TS_PID_CPU_Temp = [0] * 2* 50000
CPU_PID_CPU_Temp = [0] * 2* 50000
PID_PID_CPU_Temp = [0] * 2* 50000
Temp_PID_CPU_Temp = [0] * 2* 50000
PIDs = [0] * 2* 50000

Formatted_TS_PID_CPU_Temp =   [0] * 2* 50000
Formatted_CPU_PID_CPU_Temp =[0] * 2* 50000
Formatted_PID_PID_CPU_Temp = [0] * 2* 50000
Formatted_Temp_PID_CPU_Temp =[0] * 2* 50000

TS_PID_CPU_RT = [0] * 2* 50000
CPU_PID_CPU_RT = [0] * 2* 50000
PID_PID_CPU_RT = [0] * 2* 50000
RT_PID_CPU_RT = [0] * 2* 50000
VRT_PID_CPU_RT = [0] * 2* 50000



def plotParams(arg1, cpu, totalSamples, pid, gradient):
    #print(f"Plot Start: {info['Date']}, {info['TimeStamp']},info['value'] ")
    Samples = int(int(totalSamples)/int(gradient))
    if(arg1==1):
        x = Formatted_TS_PID_CPU_Temp[:Samples]
        y = Formatted_Temp_PID_CPU_Temp[:Samples]
        # Creating the plot
    if(arg1==2): 
        x = TS_PID_CPU_RT
        y = RT_PID_CPU_RT
        
    #print("X:", x)
    #print("Y:", y)

    x1 = np.array(x, dtype=float)
    y1= np.array(y, dtype=int)

    m, b,c = np.polyfit(x1,y1, 2)  # 2 for polynomial fit.
    trendline_x = x1 #np.linspace(min(x1), max(x1),100)  # 100 points for smooth line
    trendline_y = m * trendline_x**2 + b *trendline_x + c

    plt.plot(x, y, marker='.', linestyle=':', linewidth=2, label="CPU:" + str(cpu) + " PID:" + str(pid) + "#Samples:" + str(Samples),  markevery=len(x), color='black')
    plt.plot(x, trendline_y, '-', label='Quadratic-Fit', linewidth=2, color='red')


    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.5))
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(10))



    # Adding titles and labels
    plt.title("ProcessTemperature Vs Time")
    plt.xlabel("SystemTime")
    plt.ylabel("PerCore Temperature(degC)")
    plt.xticks(rotation=70)
    # Displaying the grid (optional)
    plt.grid(False)
    plt.legend()
    plt.tight_layout()




# Access individual argument
if len(sys.argv) > 1:
    file_path  = sys.argv[1]
    pid  = sys.argv[2]
    gradient  = sys.argv[3]

pattern1 = r'.*(\[(\d{3})\]) (\d{5}.\d{6}): bprint.*pid.(\d+), Temp:(\d+)'
pattern2 = r'.*(\[(\d{3})\]) (\d{5}.\d{6}): bprint.*pid.'+ f'({pid}), Temp:(\d+)'
pattern3 = r'.*(\[(\d{3})\]) (\d{5}.\d{6}): sched_stat_runtime.*pid=(\d+).*runtime=(\d+).*vruntime=(\d+)'

rows = 200
columns = 2*50000 


# Open the file and read line by line
No_RT = 1 
uniquePIDs = [0]*200
PIDs = [0]*200
indx = [0]*2*50000
for i in range(0,8):
    iter = 0
    iter1 = 0
    basePID = 0
    file_name = file_path + str(i) + ".txt"
    with open(file_name, 'r') as file:
    #    print(f'FilePath = {file_path}')
        for line in file:
    #       print(f'Line = {line}')
            match1 = re.findall(pattern1, line)
            for match in match1:
                TS_PID_CPU_Temp[iter] = match[2]
                CPU_PID_CPU_Temp[iter] =match[1]
                PID_PID_CPU_Temp[iter] = match[3]
                Temp_PID_CPU_Temp[iter] =100-int(match[4])
                iter = iter+1
                #print(f"CPU:{match[1]},TS:{match[2]},PID:{match[3]},Temperature:{100-int(match[4])}" )

            if No_RT == 0:
                match1 = re.findall(pattern3, line)
                for match in match1:
                    if iter1 < 2*49000:
                        TS_PID_CPU_RT[iter1] = match[2]
                        CPU_PID_CPU_RT[iter1] = match[1]
                        PID_PID_CPU_RT[iter1] = match[3]
                        RT_PID_CPU_RT[iter1] = match[4]
                        VRT_PID_CPU_RT[iter1] = match[5]
                        iter1 = iter1+1

                    print(f"CPU:{match[1]},TS:{match[2]},PID:{match[3]},ActualRuntime:{match[4]},VirtualRunTime:{match[5]}" )
        
        uniquePIDs = set(PID_PID_CPU_Temp)
        totalPIDs  = len(uniquePIDs)
        totalSamples = iter-1
        
        PIDs  = np.array(list(uniquePIDs))
        indx = 0
        match = 0

        print(f'total PIDs on CPU{i} = {totalPIDs}, total samples= {totalSamples}, {PIDs} ')
        for iterator in PIDs:
            if iterator != 0:
                for contentPerCPUIter in range(0,totalSamples):
                    if iterator == PID_PID_CPU_Temp[contentPerCPUIter] and float(TS_PID_CPU_Temp[contentPerCPUIter]) > float(Formatted_TS_PID_CPU_Temp[indx]):
                        Formatted_TS_PID_CPU_Temp[indx] =   TS_PID_CPU_Temp[contentPerCPUIter] 
                        Formatted_CPU_PID_CPU_Temp[indx] =CPU_PID_CPU_Temp[contentPerCPUIter]
                        Formatted_PID_PID_CPU_Temp[indx] = PID_PID_CPU_Temp[contentPerCPUIter]
                        Formatted_Temp_PID_CPU_Temp[indx] =Temp_PID_CPU_Temp[contentPerCPUIter] 
                        indx = indx + 1
                        match = 1

                if match==1 and (indx-1) > 100 :
                    match = 0
                    print(f'Plot prep for CPU:{i}, PID:{iterator}, Samples:{indx-1}') 
                    plotParams(1, i, indx-1, iterator, gradient )
                    plt.show()
                    indx = 0
                
        Formatted_TS_PID_CPU_Temp = [0] * 2* 50000
        Formatted_Temp_PID_CPU_Temp = [0] * 2* 50000
        Formatted_CPU_PID_CPU_Temp = [0] * 2* 50000
        Formatted_PID_PID_CPU_Temp = [0] * 2* 50000
        TS_PID_CPU_Temp = [0] * 2* 50000
        CPU_PID_CPU_Temp = [0] * 2* 50000
        PID_PID_CPU_Temp = [0] * 2* 50000
        Temp_PID_CPU_Temp = [0] * 2* 50000

try:
    while True:

        # Example condition to break the loop: wait for 5 seconds
        time.sleep(1)  # Adjust the sleep time as needed

        # Check for a condition to break the loop
        if input("Press 'q' to quit: ") == 'q':
            print("Exiting loop.")
            break
except KeyboardInterrupt:
    print("\nLoop interrupted by user.")
