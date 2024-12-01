def tu (timestamp):
    if  (timestamp >= 1 and timestamp < 12) :
        return("GOOD MORNING SIR".upper())
    elif ( timestamp >= 12 and timestamp < 16):
        return("good afternoon sir ".upper())
    elif ( timestamp > 16 and timestamp < 20):
        return("good evening sir ".upper())
    else:
        return("good night sir ".upper())
import time
timestamp = int(time.strftime('%H'))
timestop = time.strftime("%H:%M:%S")
print(timestop)
mei = tu(timestamp)
print(mei)