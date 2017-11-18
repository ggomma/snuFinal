import time
import picamera

with picamera.PiCamera() as cam:
    cam.start_preview()
    time.sleep(1)
    cam.capture('./img/face.jpg')
    cam.stop_preview()
