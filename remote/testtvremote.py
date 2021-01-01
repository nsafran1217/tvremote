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
with samsungctl.Remote(config) as remote:
    remote.control("KEY_VOLDOWN")

