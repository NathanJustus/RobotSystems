import time
from picamera import PiCamera
from io import BytesIO
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

#Class to handle repeated picture taking using Raspberry Pi
class PictureTaker():

	#Initialize camera and data stream
	def __init__(self):
		self.camera = PiCamera()
		self.camera.resolution = (400,300)
		self.camStream = BytesIO()
		self.camera.start_preview()
		time.sleep(2)

	#Take a picture, do some small preprocessing, and return picture data
	def takePicture(self):
		#Snag picture and write to stream
		self.camera.capture(self.camStream,format='jpeg')
		#Rewind stream to start of picture
		self.camStream.seek(0)
		#Convert stream data to numpy uint8 array
		file_bytes = np.asarray(bytearray(self.camStream.read()),dtype=np.uint8)
		#Convert numpy array to OpenCV structure
		img = cv.imdecode(file_bytes,cv.IMREAD_COLOR)

		#Crop image to bottom third and middle half where line probably is
		croppedImg = img[200:300,100:300]
		self.lastCrop = croppedImg
		#To grayscale
		grayImg = cv.cvtColor(croppedImg,cv.COLOR_BGR2GRAY)
		#Find edges (might have to mess with min/max thresholds)
		self.lastEdges = cv.Canny(grayImg,100,200)
		return self.lastEdges


if __name__ == "__main__":
	picTaker = PictureTaker()

	img = picTaker.takePicture()
	crop = picTaker.lastCrop
	plt.subplot(211)
	plt.imshow(crop,cmap='gray')
	plt.subplot(212)
	plt.imshow(img,cmap='gray')
	plt.show()
	time.sleep(2)
