import cv2
import time
import warnings
warnings.simplefilter("ignore")

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
