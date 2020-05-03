import os
import time
from datetime import datetime
import re
import sys
file = open("/home/pi/StatsLog.txt", "a")




file.write("-"*15)
file.write(" \n")
file.write(time.strftime("%x"))
file.write(" \n")
file.write(time.strftime("%X"))
file.write(" \n")
file.write(" \n")


def measure_temp():
	temp = os.popen("vcgencmd measure_temp").readline()
	return (temp.replace("temp=",""))
		
def measure_volts():
	volts = os.popen("vcgencmd measure_volts core").readline()
	return (volts.replace("volts=",""))
		
def measure_speed():
	speed = os.popen("vcgencmd measure_clock arm").readline()
	return (speed.replace("speed=",""))
		
def mem_arm():
	memarm = os.popen("vcgencmd get_mem arm").readline()
	return (memarm.replace("memarm=",""))
	
def mem_gpu():
	memgpu = os.popen("vcgencmd get_mem gpu").readline()
	return (memgpu.replace("memgpu=",""))	
	



file.write("CORE TEMP\n")
file.write(measure_temp())
file.write(" \n")
file.write("--$--$--$--$--$--\n")
file.write("VOLTS\n")
file.write(measure_volts())
file.write(" \n")
file.write("--$--$--$--$--$--\n")
file.write(" \n")
file.write("CLOCK SPEED\n")
file.write(measure_speed())
file.write(" \n")
file.write("--$--$--$--$--$--\n")
file.write("ARM MEMORY\n")
file.write(mem_arm())
file.write(" \n")
file.write("--$--$--$--$--$--\n")
file.write("GPU MEMORY\n")
file.write(mem_gpu())
file.write("--$--$--$--$--$--\n")
file.write(" \n")




# Transforms the value read in integer
TEMPa = os.popen("vcgencmd measure_temp").readline()
#TEMPb = re.findall(r'\d+', TEMPa)
#TEMPc = list(map(int, TEMPb))
#TEMPd = TEMPc[1:]
TEMP = TEMPa.startswith("7",5,) 

file.write(TEMPa)
file.write(" \n")

# Sets supported maximum temperature
# MAX= 70

# file.write ("Too hot?" TEMP)

if 	TEMP == True:

		
		file.write ("This is too hot!")
		
#		time.sleep(60)

		# Halt hardware
#
		os.system("sudo shutdown -h now")
else:
		# Remove lock

		file.write ("No issue to report\n")
		sys.exit()

