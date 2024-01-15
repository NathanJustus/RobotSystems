from time import sleep
from picamera import PiCamera
from io import BytesIO
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

camStream = BytesIO()
cam = PiCamera()
cam.start_preview()
sleep(2)

for i in range(3):
	cam.capture(camStream,format='jpeg')
	camStream.seek(0)
	file_bytes = np.asarray(bytearray(camStream.read()),dtype=np.uint8)
	img = cv.imdecode(file_bytes,cv.IMREAD_COLOR)
	camStream.seek(0)

	edges = cv.Canny(img,100,200)

	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print(current_time)
	
	subplotID = int('13'+str(i+1))
	plt.subplot(subplotID)
	plt.imshow(img,cmap='gray')
	plt.title('Image '+str(i+1))

plt.show()
