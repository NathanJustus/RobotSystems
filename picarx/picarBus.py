# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:01:07 2024

@author: Nathan Justus
"""
from readerwriterlock import rwlock

class PicarBus():
    
    def __init__(self,initialMessage="Not set yet"):
        self.message = initialMessage
        self.lock = rwlock.RWLockWriteD()
        
    def write(self,msg):
        with self.lock.gen_wlock():
            self.message = msg
        
    def read(self):
        with self.lock.gen_rlock():
            msg = self.message
        return msg