# Micropython_MP3_Speaker
I was looking around to implement a motion based MP3 loudspeaker box to place it some corner of my bathroom so every time I enter it it plays some music.
So I came to the DFPlayer modul which I added to one of my WemosD1 Mini.
I also added a PIR sensor for motion detectin and an LDR because I don'w want the music played in the night.<BR>
So this is the elctrical setup:<BR><BR>
![](https://github.com/Fiege/Micropython_MP3_Speaker/blob/master/MP3_Player_Schaltplan.png?raw=true)
  
About the code:
I took two files for the serial communication an the MP3 player control from this Github repo and added my own main.py to it (thank to mlupo):

https://github.com/mlupo/micropython-yx5300
