# tvremote.py
#https://github.com/xchwarze/samsung-tv-ws-api
#token = 10397787 #THIS IS FOR PROXY 10.35.0.165
from samsungtvws import SamsungTVWS
from threading import Timer
import threading

tvIP = '10.35.0.13' 
tvPort = 8002
tvToken = 10397787

def CheckSleep():

    for x in threading.enumerate():
        if x.name == "TvTimerThread":
            return "A sleep timer is set"
        else:
            return "Make a selection"

def PowerOff():
    try:
        tv = SamsungTVWS(host=tvIP, port=tvPort, token=tvToken)
        tv.shortcuts().power()
        return "Power Pressed"
    except Exception as e:
        return "Error: "+ str(e)

def VolUp():
    try:
        tv = SamsungTVWS(host=tvIP, port=tvPort, token=tvToken)
        tv.shortcuts().volume_up()
        return "Volume Up Pressed"
    except Exception as e:
        return "Error: "+ str(e)        

def VolDown():
    try:
        tv = SamsungTVWS(host=tvIP, port=tvPort, token=tvToken)
        tv.shortcuts().volume_down()
        return "Volume Down Pressed"
    except Exception as e:
        return "Error: "+ str(e)

def Mute():
    try:
        tv = SamsungTVWS(host=tvIP, port=tvPort, token=tvToken)
        tv.shortcuts().mute()
        return "Mute Pressed"
    except Exception as e:
        return "Error: "+ str(e)      

def Sleep(time):
    try:
        for x in threading.enumerate():
            if x.name == "TvTimerThread":
                x.cancel()  
        if int(time) == 0:
            return "Sleep cancled" 
        timeseconds = int(time) * 60
        timer = Timer(timeseconds, PowerOff)
        timer._name = "TvTimerThread"
        timer.start()
        return f"TV will turn off in {time} minutes"
    except Exception as e:
        return "Error: "+ str(e)

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   PowerOff()
   VolUp()
   VolDown()
   Sleep()
   Mute()
   CheckSleep()
