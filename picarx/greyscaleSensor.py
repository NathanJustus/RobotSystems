import picarBus
import time

# -*- coding: utf-8 -*-
class GreyscaleSensor():
    
    def __init__(self,car):
        self.mycar = car
    
    def readSensors(self):
        return self.mycar.get_grayscale_data()
    
    def produceData(self,gsDataBus,delay):
        while True:
            
            vals = self.readSensors()
            gsDataBus.write(vals)
            
            print(f'Read Data:{vals}')
            time.sleep(delay)