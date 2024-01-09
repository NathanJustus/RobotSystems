# -*- coding: utf-8 -*-
class GreyscaleSensor():
    
    def __init__(self,car):
        self.mycar = car
    
    def readSensors(self):
        return self.mycar.get_grayscale_data()