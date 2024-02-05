#Countdown Timer

import time


My_Time = int(input("Enter the time in Seconds : "))

for x in range(My_Time,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    print (f"00:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's Over")