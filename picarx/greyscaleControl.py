# -*- coding: utf-8 -*-

import picarx_improved as pc
import time
import numpy as np
import atexit
import concurrent.futures
import threading

from greyscaleSensor import GreyscaleSensor as GS
from greyscaleSensorInterpreter import GreyscaleSensorInterpreter as GSI
from picarBus import PicarBus


class GreyscaleController():
    
    def __init__(self,car,steerMag = 20):
        self.steerMag = steerMag
        self.car = car
        
    def doControl(self,error):
        car = self.car
        
        angleCommand = self.steerMag*error
        
        car.set_dir_servo_angle(angleCommand)
        return angleCommand
    
    def consume(self,gsErrorBus,delay,exitEvent):
        while True:
            print('Doing Control')
            error = gsErrorBus.read()
            angleCommand = self.doControl(error)
            self.car.set_dir_servo_angle(angleCommand)
            car.forward(45)
            
            if exitEvent.isSet():
                car.stop()
                break
            
            time.sleep(delay)
            
        
if __name__ == "__main__":
    car = pc.Picarx()
    sensor = GS(car)
    interpreter = GSI(80,'tapeDarker')
    controller = GreyscaleController(car,30)
    atexit.register(car.stop)
    
    loopHz = 1
    delayTime = 1/loopHz
    
    gsDataBus = PicarBus([0,0,0])
    gsErrorBus = PicarBus(0)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:   
        eSensor = executor.submit(sensor.produceData,gsDataBus,delayTime)
        #eInterpreter = executor.submit(interpreter.consumeProduce,gsDataBus,gsErrorBus,delayTime)
        #eController = executor.submit(controller.consume,gsErrorBus,delayTime)
        print('Howdydowdy')

    eSensor.result()
    #eInterpreter.result()
    #eController.result()
        