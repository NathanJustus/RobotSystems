# -*- coding: utf-8 -*-

import picarx_improved as pc
import time

mycar = pc.Picarx()

while True:
    print(mycar.get_grayscale_data())
    time.sleep(0.25)
    