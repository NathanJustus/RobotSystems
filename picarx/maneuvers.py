import picarx_improved as pcx
import time

def parkRight(car):
	car.stop()
	car.set_dir_servo_angle(0)
	car.forward(50)
	time.sleep(2)
	car.stop()

	angleRange = [-30,25]
	car.set_dir_servo_angle(angleRange[0])
	time.sleep(0.5)

	car.backward(50)
	for i in range(angleRange[0],angleRange[1]):
		car.set_dir_servo_angle(i)
		time.sleep(.05)

	car.stop()
	car.set_dir_servo_angle(0)


if __name__ == "__main__":
	exitFlag = false
