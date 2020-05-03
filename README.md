# RPi_statslog
A stats log and auto temp shut-down of RPi

I am not the best coder in the world, this is a hobby, this is far from elegant.  This will produce a stats log in the /home/pi/ folder.  This script will also shut down if the temp gets to 70c.  This isn't the best way f doing it but I was dragging the temp with the unit and had to convert into a readable number.  I did this by selecting the '10's' value and if it equals '7' a shut-down will occur.  In the unlikely event that there is a jump from 69.9 to 80.0 then, well, I suppose I could add another line.

First, download the PiMonitor.py into /home/pi/

I have then used 

crontab -e

to run this scipt every 5 minutes by using 

*/5 * * * * sudo python /home/pi/PiMonitor.py

You could change the crontab to change the interval, I have this set to every minute on heavy usages RPi's.

When this has run, it amends a file /home/pi/statslog.txt added the current stats to the end.  Eg.

--------------- 
05/03/20 
09:45:02 
 
CORE TEMP
37.9'C
 
--$--$--$--$--$--
VOLTS
volt=1.3500V
 
--$--$--$--$--$--
 
CLOCK SPEED
frequency(45)=1000000000
 
--$--$--$--$--$--
ARM MEMORY
arm=448M
 
--$--$--$--$--$--
GPU MEMORY
gpu=64M
--$--$--$--$--$--
 
temp=37.9'C
 
No issue to report
