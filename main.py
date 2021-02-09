import FileChecker
import Music
import time
import GPIO
import Dummy


class main:

    def cycle(self):

        # Sets the play time onto the lcd screen
        self.pins.setOutput(self.music.getCurPlayTime())

        # Check to see if there is a file named "Play"
        if self.fc.checkPlay():
            self.music.play()

        # Check to see if there is a file named "Pause"
        if self.fc.checkPause():
            self.music.pause()

        # Check to see if there is a file named "Volume Up"
        if self.fc.checkVolumeUp():
            self.music.volumeUp()

        # Check to see if there is a file named "Volume Down"
        if self.fc.checkVolumeDown():
            self.music.volumeDown()

    # I think this is for updating the LCD screen?
    def timeLoop(self):
        t = time.time()
        if t > self.nextCheck:
            self.nextCheck = t + 10000
            print("THIS IS NOT RIGHT! NEED TO FIX!!!")
            self.pins.setOutput("FUCK! THIS IS WRONG")

    #
    def init(self, onPi):
        self.fc = FileChecker.FileChecker()

        # GPIO class only works Raspberry pi.
        # If this is not being ran on a pi, use a dummy module.
        if onPi:
            self.pins = GPIO.gpio()
            self.fc.init("/home/pi")
        else:
            self.pins = Dummy.Dummy()
            self.fc.init("/home/chesspro13")

        # Controls music
        self.music = Music.Music()
        self.music.init()

        # Time keeping
        self.nextCheck = 0


        # Main loop for the program
        while True:
            self.cycle()
            #    time.sleep(0.0001)


# Start Program
p = main()
# Boolean is used to determine if the script is being running on raspberry pi or now.
p.init(False)
