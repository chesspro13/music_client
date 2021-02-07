from subprocess import call
from lcddriver import lcd
import sys
import os

from youtube_dl import YoutubeDL
from bs4 import BeautifulSoup
import requests

import sys
import pafy
import time

import vlc
from time import sleep

import RPi.GPIO as gpio
button = 40

url = input("What is the youtube download link?")

playing = False

def getData(url):
    response = requests.get(url)
    soup = BeautifulSoup( response.text, 'html.parser')#, 'lxml')
    m = soup.find("title")
    print( m.text.replace("<title>","").replace(" - YouTube","") )

def downloadAudio(url):
    video = pafy.new(url)
    audio = video.getbestaudio()
    audio.download()

indexA = 0
indexB = 0

my_lcd = lcd()

lastA = ""
lastB = ""

songName = ""

p = None

def getTime():
    return( round(time.time() *1000))

def setOutput():
    global indexA
    global indexB
    global my_lcd
    global lastA
    global lastB
    global songName
    output1 = "<This is output>"

    output2 = "<I like bananas>"

    my_lcd.clear()

    try:
        print( str(int(p.get_time()/1000 )) + "/" + str(int(p.get_length()/1000)))
        per = '{:.1%}'.format(int(p.get_time()/1000 ) / int(p.get_length()/1000))
    except:
        print( output2 )
        per = "Calibrating..."

    output2 = per

#   if output2 != lastB:
    if len(output2) < 17:
        my_lcd.display_string( output2, 1)
        lastB = output2
    else:
        if indexB == len( output2 ):
            indexB = 0
        txt = output2[indexB: indexB + 16]
        my_lcd.display_string( txt, 1)
        indexB += 1
        lastB = txt

    if len(songName) < 17:
        my_lcd.display_string( songName, 2)
    else:
        if indexA == len( songName ):
            indexA = 0
        txt = songName[indexA: indexA + 16]

        if len(output) - indexA < 16:
            for i in range( len( output) + 16 ):
                txt += " "

        my_lcd.display_string( txt, 2)
        indexA += 1

volume = 100

def volumeDown():
    global volume

    if volume > 1:
        volume -= 10

    call( ["amixer", "-D", "pulse", "sset", "Master",str(volume)+"%"] )

def volumeUp():
    global volume

    if volume < 99:
        volume += 10

    call( ["amixer", "-D", "pulse", "sset", "Master",str(volume)+"%"] )

png = 0
def switchText():
    if png == 0:
        songName = "This is a song name"
    elif png == 1:
        songName = "Farting feels like angel tongue"
    elif png == 2:
        songName = "This is a really big apple"
    else:
        songName = "How the fuck did you get here???"

    png += 1
    indexA = 0
    indexB = 0

waitingForButton = False
nextButton = getTime()

def toggleButton():
    global nextButton
    global waitingForButton
    if getTime() > nextButton:
        togglePlay()
        waitingForButton = False

    if waitingForButton == False:
        nextButton = getTime() + 1000
        waitingForButton = True

hasLength = False
nextCheck = 0

def setCurPos():
    global p
    global nextCheck

    if time.time() > nextCheck:
        f = open("/home/pi/commands/curTime", "w")
        s = f.write(str(p.get_time()))
        f.close()
        nextCheck = time.time() + 500;



def cycle():
    global hasLength
#   setOutput(url)
    if p.get_length() < 10:
        writeLength()        
    else:
        if hasLength == False:
            hasLength = True;
            writeLength()

    setCurPos()

    butt = gpio.input( 10 )
    if butt == gpio.HIGH:
#       swtichText()
        toggleButton()
        print( "toggle button" )


    if os.path.isfile("/home/pi/commands/play"):
        play()
        os.system( "sudo rm /home/pi/commands/play")

    if os.path.isfile("/home/pi/commands/stop"):
        stop()
        os.system( "sudo rm /home/pi/commands/stop")
    
    if os.path.isfile("/home/pi/commands/volumeUp"):
        volumeUp()
        os.system( "sudo rm /home/pi/commands/volumeUp")

    if os.path.isfile("/home/pi/commands/volumeDown"):
        volumeDown()
        os.system( "sudo rm /home/pi/commands/volumeDown")

    if os.path.isfile("/home/pi/commands/getTime"):
        getMusicTime()
        os.system( "sudo rm /home/pi/commands/getTime");

def getMusicTime():
    global p

    f = open("/home/pi/commands/time", "w")
    f.write( str(p.get_time() ))
    f.close()

def togglePlay():
    global playing
    global p
    if playing:
        p.set_pause(1)
        playing = False
    else:
        p.set_pause(0)
        playing = True
    print( "Toggled")

def loadMusic():
    global p
    global songName
    p = vlc.MediaPlayer("/home/pi/low.mp3")
    songName = "Lofi Sleep"

def writeLength():
    global p
    f = open("/home/pi/commands/audioLength", "w")
    print("Length according to now: " + str(p.get_length()))
    f.write( str(p.get_length() ))
    f.close()


def play():
    global p
    global playing
#   p.set_pause(0)
    p.play()
    playing = True

def stop():
    global p
    global playing
    p.set_pause(1)
    playing = False

def init():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_DOWN)

init()
loadMusic()
play()
nextCheck = 0



#getData( url )
while True:
    cycle()
#    time.sleep(0.0001)
    if getTime() > nextCheck:
        nextCheck = getTime() + 2500
        setOutput()

    

