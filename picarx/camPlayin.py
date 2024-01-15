from time import sleep
from picamera import PiCamera
from io import BytesIO
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

camStream = BytesIO()
cam = PiCamera()
cam.resolution = (400,300)
cam.start_preview()
sleep(2)

nPics = 1
for i in range(nPics):
	cam.capture(camStream,format='jpeg')
	camStream.seek(0)
	file_bytes = np.asarray(bytearray(camStream.read()),dtype=np.uint8)
	img = cv.imdecode(file_bytes,cv.IMREAD_COLOR)
	camStream.seek(0)

	crop = img[225:300,125:275]
	gray=cv.cvtColor(crop,cv.COLOR_BGR2GRAY)
	edges = cv.Canny(gray,100,200)
	im2,contours = cv.findContours(edges,cv.RETR_CCOMP,cv.CHAIN_APPROX_SIMPLE)
	
	cv.drawContours(img,contours,-1,(0,255,0),3)

	#subplotID = int('13'+str(i+1))
	#plt.subplot(subplotID)
	#plt.imshow(edges,cmap='gray')
	#plt.title('Image '+str(i+1))

#plt.show()
