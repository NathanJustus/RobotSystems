# -*- coding: utf-8 -*-

import picarx_improved as pc
import time
import numpy as np

from greyscaleSensor import GreyscaleSensor as GS
from greyscaleSensorInterpreter import GreyscaleSensorInterpreter as GSI

class GreyscaleController():
    
    def __init__(self,car,steerMag = 20):
        self.steerMag = steerMag
        self.car = car
        
    def doControl(self,error):
        car = self.car
        
        angleCommand = self.steerMag*error
        
        car.set_dir_servo_angle(angleCommand)
        return angleCommand
    
if __name__ == "__main__":
    car = pc.Picarx()
    sensor = GS(car)
    interpreter = GSI(85,'tapeDarker')
    controller = GreyscaleController(car,30)
    
    while(True):
        rawData = sensor.readSensors()
        interpreter.updateState(rawData)
        error = interpreter.getCarPosition()
        controller.doControl(error)
        car.forward(35)
        time.sleep(0.01)