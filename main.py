#This file is part of Micropython_MP3_Speaker
#
#    Micropython_MP3_Speaker is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    Micropython_MP3_Speaker is (c) copyright 2020 by U. Fiege

import machine
import socket
import ure
import mp3
import time
from machine import Pin

 

lvlDark = 3 # At which level of light the music should not play
playVol = 12 #12
bsy = Pin(0, Pin.IN)
brght = machine.ADC(0)
snsMove = Pin(5, Pin.IN) 
brnow, br1,br2,br3,br4,br5,br6,br7,br8,br9,br10  = 0,0,0,0,0,0,0,0,0,0,0


mp3.set_volume(playVol)
mp3.pause()


while True:
    br1=br2
    br2=br3
    br3=br4
    br4=br5
    br5=br6
    br6=br7
    br7=br8
    br8=br9
    br9=br10
    try:
        br10=brght.read()
        brnow = int((br1 + br2+ br3 + br4 + br5 + br6 + br7 + br8 + br9 + br10) / 10)
        print ("busy:",bsy.value(), "  brightness:", brnow, "(", br10 , ")  sensor 2:", snsMove.value())
        if (brnow >= lvlDark): # es ist hell
            if (snsMove.value()==0): #no movement
                if (bsy.value()==0): # it is playing
                    print("pausing")
                    mp3.pause()
                #endif
            else: #movement detected
                if (bsy.value()==1): # it is not playing
                    print("playing next track")
                    mp3.set_volume(playVol)
                    mp3.next()
                #endif
            #endif
        else: #es ist dunkel, schalte musik ab, falls sie spielt
            if (bsy.value()==0): # it is playing
                print("pausing")
                mp3.pause()
            #endif
        #endif
    #endtry
    except Exception as err:
        print ("Error occured :" , str(err))
    #endexcept    
    time.sleep(.5)
