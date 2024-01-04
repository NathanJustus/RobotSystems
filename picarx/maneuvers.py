import picarx_improved as pcx
import time

def parkLeft(car):
	car.stop()
	car.set_dir_servo_angle(0)
	car.forward(50)
	time.sleep(1)
	car.stop()

	angleMag = 30
	angleRange = [-angleMag,angleMag]
	car.set_dir_servo_angle(angleRange[0])
	time.sleep(0.5)

	car.backward(50)
	for i in range(angleRange[0],angleRange[1]):
		car.set_dir_servo_angle(i)
		time.sleep(.05)

	car.stop()


if __name__ == __main__:
	exitFlag = false
