import cv2
import time
import warnings
import requests
from requests.exceptions import HTTPError
from datetime import datetime
import json
warnings.simplefilter("ignore")

server_url = ""


def setStatus(self, hwid, status):
    payload = {
        'hwid': str(hwid),
        'timestamp': datetime.timestamp(datetime.now()),
        'status': status
    }
    headers = {'content-type': 'application/json'}
    response = requests.request(
        "POST", server_url, data=json.dumps(payload), headers=headers)
    return json.loads(response.text)


def monitorCam():
    while(True):
        try:
            vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            if not vc.isOpened:
                raise IOError("cant Open")
            else:
                stat, frame = vc.read()
                vc.release()
                if(not stat):
                    raise IOError("cant Open")
        except Exception as ex:
            print("\nerror found:", ex, "\n")
        time.sleep(5)


if __name__ == "__main__":
    monitorCam()
