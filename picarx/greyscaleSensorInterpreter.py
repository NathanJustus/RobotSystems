# -*- coding: utf-8 -*-

import picarx_improved as pc
import time

class GreyscaleSensorInterpreter():

    def __init__(sens=30,polarity='tapeDarker'):
        self.tapeState = [False,False,True,False,False]
        self.sensitivity = sens
        self.polarity = polarity
        self.lastReading = [0,0,0]

    def updateState(dataReading):
        lr = self.lastReading
        if sum(abs(lr)) == 0:
            self.lastReading = dataReading
            pass

        

while True:
    print(mycar.get_grayscale_data())
    time.sleep(0.25)
    