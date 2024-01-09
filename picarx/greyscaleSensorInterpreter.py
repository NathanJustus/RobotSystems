# -*- coding: utf-8 -*-

import picarx_improved as pc
import time
import numpy as np

class GreyscaleSensorInterpreter():

    def __init__(self,sens=25,polarity='tapeDarker'):
        self.tapeState = [False,False,True,False,False]
        self.sensitivity = sens
        self.lastReading = [0,0,0]
        
        if polarity == 'tapeDarker':
            self.polarity = -1
        elif polarity == 'tapeLighter':
            self.polarity = 1
        else:
            raise ValueError('Polarity must be either "tapeDarker" or "tapeLighter".')

    def updateState(self,dataReading):
        
        lr = np.array(self.lastReading)
        if sum(abs(lr)) == 0:
            self.lastReading = dataReading
            pass
        
        dr = np.array(dataReading)
        diff = lr - dr
        diff = diff*self.polarity
        self.lastReading = dataReading
        
        newDetects = diff < (-1*self.sensitivity)
        lostDetects = diff > (self.sensitivity)
        
        oldState = self.tapeState
        state = oldState
        
        if newDetects[1]:
            state = [False,False,True,False,False]
        elif newDetects[0]:
            state = [False,True,False,False,False]
        elif newDetects[2]:
            state = [False,False,False,True,False]
            
        if lostDetects[0]:
            if oldState[1] and not newDetects[1]:
                state = [True,False,False,False,False]
            else:
                state[1] = False
        if lostDetects[1]:
            state[2] = False
        if lostDetects[2]:
            if oldState[3] and not newDetects[1]:
                state = [False,False,False,False,True]
            else:
                state[3] = False
                
        self.tapeState = state
        
    def getCarPosition(self):
        
        state = self.tapeState
        
        if state[0]:
            return 1
        if state[4]:
            return -1
        
        if state[1]:
            return .5
        if state[3]:
            return -.5
            
        return 0
        
if __name__ == "__main__":  
    car = pc.Picarx()
    sens = GreyscaleSensorInterpreter(25,'tapeDarker')
    while True:
        reading = car.get_grayscale_data()
        sens.updateState(reading)
        state = sens.getCarPosition()
        
        print(state)
        time.sleep(0.25)
    