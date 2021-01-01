# tvremote.py
#token = 10397787 #THIS IS FOR PROXY 10.35.0.165
from samsungtvws import SamsungTVWS
from threading import Timer

tv = SamsungTVWS(host='10.35.0.13', port=8002, token=10397787)

def PowerOff():
    try:
        tv.shortcuts().power()
        return "TV Turned Off"
    except Exception as e:
        return "Error: "+ str(e)

def VolDown():
    try:
        tv.shortcuts().volume_down
        return "Volume Down Pressed"
    except Exception as e:
        return "Error: "+ str(e)

def Sleep(time):
    try:
        timeseconds = int(time) * 60
        timer = Timer(timeseconds, PowerOff)
        timer.start()
        return f"TV Will turn off in {time} minutes"
    except Exception as e:
        return "Error: "+ str(e)
     


if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   PowerOff()
   VolDown()
   Sleep()