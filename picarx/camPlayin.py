from io import BytesIO
from time import sleep
from picamera import PiCamera

camStream = BytesIO()
cam = PiCamera()
cam.start_preview()
sleep(2)

img = cam.capture(camStream,'jpeg')
print(img)