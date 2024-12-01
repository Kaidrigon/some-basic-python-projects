#a voting system idk
import pyttsx3 
enlip = pyttsx3.init()
voices = enlip.getProperty('voices')
enlip.setProperty('voice', voices[33].id)  
enlip.setProperty('rate', 150)
enlip.say("Do you, want to give vote yes or no only sir")
print("do you, wanna give vote my majesty")
enlip.runAndWait()
x=input()
if (x == "yes"):
    enlip.say("who? you have two options team 1 who is a national government and team 2 who is chutiya i don't know sir ")
    enlip.runAndWait()
    u = int(input("enter 1 or 2"))
    if( u == 1):
        enlip.say("CONGRATULATIONS!!!!, NOW YOU ARE ALSO THE PART OF SLIUMS YAAY GREEB")
        enlip.runAndWait()
    elif( u==2):
        enlip.say("YA GREEB ISKI MA KI CH- CONGRATS NOW NOTHING IS CHANGED YOU ARE STILL A PIECE OF SHIT BUT ATLEAST YOU WON!!!!")
        enlip.runAndWait()
    else:
        enlip.say("yo white ass dude look you what you did you illetrate brat ")
        enlip.runAndWait()
else:
    enlip.say("ok thanks for coming")
    enlip.runAndWait()