from time import sleep
from picamera import PiCamera, CircularIO

camStream = CircularIO()
cam = PiCamera()
cam.start_preview()
sleep(2)

cam.capture(camStream,'jpeg')
img = camStream.array()
print(img)