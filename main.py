import IRInterface
import FileChecker
import Music
import time
import GPIO
import Dummy


class main:

    def cycle(self):

        # Sets the play time onto the lcd screen
        if self.hasGpio:
            self.pins.setOutput(self.music.getCurPlayTime(), 1)

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

        if self.fc.checkGetTime():
            self.fc.setTotalPlayTime(self.music.getTotalPlayTime())

    # I think this is for updating the LCD screen?
    def timeLoop(self):
        t = time.time()
        if t > self.nextCheck:
            self.nextCheck = t + 10000
            print("THIS IS NOT RIGHT! NEED TO FIX!!!")
            self.pins.setOutput("FUCK! THIS IS WRONG")

    def init(self, onPi):
        self.hasGpio = False
        self.hasIR = True

        self.fc = FileChecker.FileChecker()

        # Controls music
        self.music = Music.Music()
        self.music.init()

        # GPIO class only works Raspberry pi.
        # If this is not being ran on a pi, use a dummy module.
        if onPi:
            if self.hasGpio:
                self.pins = GPIO.GPIO()
                self.pins.init()
            self.fc.init("/home/pi", self.music)
        else:
            self.pins = Dummy.Dummy()
            self.fc.init("/home/chesspro13", self.music)

        if self.hasIR:
            self.ir = IRInterface.IRInterface()
            self.ir.init(18, self.fc, self.music)

        # Main loop for the program
        while True:
            self.cycle()
            time.sleep(0.001)


# Start Program
p = main()
# Boolean is used to determine if the script is being running on raspberry pi or now.
p.init(True)
