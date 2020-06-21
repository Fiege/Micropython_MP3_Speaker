I was looking around to implement a motion based MP3 loudspeaker box to place it some corner of my bathroom so every time I enter it it plays some music. <BR><BR>
So I came to the DFPlayer modul which I added to one of my WemosD1 Mini. <BR>
It plays mp3 files stored on an micro SD card, could directly connected to a loudspeaker and is controlled using commands send by a serial connection. <BR>
I also added a PIR sensor for motion detection and an LDR because I don't want the music played in the night.<BR><BR><BR>
So this is the elctrical setup:<BR><BR>
![](https://github.com/Fiege/Micropython_MP3_Speaker/blob/master/MP3_Player_Schaltplan.png?raw=true)
  <BR><BR>
About the code: <BR><BR>
I took two files for the serial communication and the MP3 player control from the project in this Github repo and added my own main.py to it (thank to mlupo): <BR>

https://github.com/mlupo/micropython-yx5300
<BR><BR>
The rest is straight forward I took check the level of brightness by taking the average of 10 measured values and if it is beyond the level defined in “lvlDark”  variable and a motion is detected it will play the next audio track if the device isn’t currently playing. If the player module is currently playing or not could be determined by checking the busy status on pin 16.<BR><BR>
The variable “playVol” defines the volume level used for playback. <BR><BR>
 I connected my ESP to my WiFi just to connect to it and check the status. For that I added the printout of the current action and status in the main loop. Just use WebRepl to connect to the device. <BR><BR>
I use the 1.12 branch of MicroPython. <BR><BR>
To get it running, flash you ESP with Micropython, connect it to your WiFi, put the hardware together, copy some mp3 files to an SD card upload the three files to your ESP and give it a try. <BR><BR>

Have fun with it.

