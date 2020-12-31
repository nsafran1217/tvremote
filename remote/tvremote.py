# tvremote.py
import samsungctl
from threading import Timer

import sys

config = {
    "name": "samsungctl",
    "description": "PC",
    "id": "",
    "host": "10.35.0.13",
    "port": 8002,
    "method": "websocket",
    "timeout": 2,
}

def PowerOff():
    try:
        with samsungctl.Remote(config) as remote:
            remote.control("KEY_POWER")
            return "TV Turned Off"
    except Exception as e:
        return "Error: "+ str(e)

def VolDown():
    try:
        with samsungctl.Remote(config) as remote:
            remote.control("KEY_VOLDOWN")
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