import picarx_improved as pcx
import time

def parkRight(car):
	car.stop()
	car.set_dir_servo_angle(0)
	car.forward(50)
	time.sleep(1.9)
	car.stop()

	angleRange = [-30,26]
	car.set_dir_servo_angle(angleRange[0])
	time.sleep(0.1)

	car.backward(50)
	for i in range(angleRange[0],angleRange[1]):
		car.set_dir_servo_angle(i)
		time.sleep(.05)

	car.stop()
	car.set_dir_servo_angle(0)

def parkLeft(car):
	car.stop()
	car.set_dir_servo_angle(0)
	car.forward(50)
	time.sleep(1.9)
	car.stop()

	angleRange = [30,-26]
	car.set_dir_servo_angle(angleRange[0])
	time.sleep(0.1)

	car.backward(50)
	for i in range(angleRange[0],angleRange[1],-1):
		car.set_dir_servo_angle(i)
		time.sleep(.05)

	car.stop()
	car.set_dir_servo_angle(0)

def goForward(car):
	car.stop()
	car.set_dir_servo_angle(0)
	car.forward(100)
	time.sleep(1)
	car.stop()

def veerRight(car):
	car.stop()
	car.set_dir_servo_angle(-15)
	car.forward(100)
	time.sleep(1)
	car.stop()
	car.set_dir_servo_angle(0)

def veerLeft(car):
	car.stop()
	car.set_dir_servo_angle(15)
	car.forward(100)
	time.sleep(1)
	car.stop()
	car.set_dir_servo_angle(0)

def goBackward(car):
	car.stop()
	car.set_dir_servo_angle(0)
	car.backward(100)
	time.sleep(1)
	car.stop()

def veerBackRight(car):
	car.stop()
	car.set_dir_servo_angle(-15)
	car.backward(100)
	time.sleep(1)
	car.stop()
	car.set_dir_servo_angle(0)

def veerBackLeft(car):
	car.stop()
	car.set_dir_servo_angle(15)
	car.backward(100)
	time.sleep(1)
	car.stop()
	car.set_dir_servo_angle(0)

def kTurnLeft(car):
	car.stop()
	car.set_dir_servo_angle(20)
	car.forward(50)
	time.sleep(2)
	car.stop()
	car.set_dir_servo_angle(-20)
	car.backward(50)
	time.sleep(3)
	car.stop()
	car.set_dir_servo_angle(0)
	car.forward(50)
	time.sleep(1)

def kTurnRight(car):
	car.stop()
	car.set_dir_servo_angle(-20)
	car.forward(50)
	time.sleep(2)
	car.stop()
	car.set_dir_servo_angle(20)
	car.backward(50)
	time.sleep(3)
	car.stop()
	car.set_dir_servo_angle(0)
	car.forward(50)
	time.sleep(1)

if __name__ == "__main__":
	car = pcx.Picarx()
	exitFlag = False
	while not exitFlag:
		command = input('Watchu need?\n')
		match command:
			case 'parkRight':
				parkRight(car)
			case 'parkLeft':
				parkLeft(car)
			case 'goForward':
				goForward(car)
			case 'veerRight':
				veerRight(car)
			case 'veerLeft':
				veerLeft(car)
			case 'goBackward':
				goBackward(car)
			case 'veerBackRight':
				veerBackRight(car)
			case 'veerBackLeft':
				veerBackLeft(car)
			case 'kTurnLeft':
				kTurnLeft(car)
			case 'kTurnRight':
				kTurnRight(car)
			case 'exit':
				exitFlag = True
			case _:
				print('Invalid command\n')
