from time import sleep
from picamera import PiCamera
from io import BytesIO
from PIL import Image
import cv2 as cv
from matplotlib import pyplot as plt

camStream = BytesIO()
cam = PiCamera()
cam.start_preview()
sleep(2)

for i in range(3):
	cam.capture(camStream,format='jpeg')
	camStream.seek(0)
	img = Image.open(camStream)
	img = cv.imdecode(img)
	print(img)
	print('\n')
	sleep(1)