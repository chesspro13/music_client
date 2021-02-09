from sweetpi_I2C_scripts.lcddriver import lcd
if False:
    import Rpi.GPIO as gpio
import Music as music
import time


class GPIO:

    # If button has been pressed toggle the state of the music playing
    def checkButton(self):
        if self.butt == gpio.HIGH:
            music.toggle()

    # Prepares the strings for output to LCD
    def setOutput(self, output, line):
        # Dummy output in case something goes wrong
        dummyOutput1 = "Chesspro13's PS1"
        dummyOutput2 = "<I like bananas>"

        per = None

        playTime = int(self.musicController.getCurPlayTime() / 1000)
        totalTime = int(self.musicController.getTotalPlayTime() / 1000)

        if totalTime == 0:
            per = dummyOutput1
        else:
            per = '{:.1%}'.format( playTime / totalTime )
        self.displayText(per,1)

        try:
            songName = self.musicController.getSongName()
        except:
            songName = dummyOutput2
        finally:
            self.displayText(songName, 2)


    #Uses sweetpi's scripts to set output of LCD
    def displayText(self, output, line):

        if len(output) < 17:
            self.lcdOutput.display_string(output, line)
        else:
            if self.index[line] == len(output):
                txt = output[self.inxex[line]: self.index[line] + 16]
                self.lcdOutput.display_string(txt, 1)
                self.index[line] += 1
                self.lastOutput[line] = txt

    def toggleButton(self):
        t = time.time()
        if t > self.nextButtonPress:
            self.musicController.toggle()
            self.waitingForButton = False

        if self.waitingForButton == False:
            self.nextButtonPress = t + 1000
            self.waitingForButton = True

    def init(self):
        gpio.setwarnings(False)
        gpio.setmode(gpio.BOARD)
        gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_DOWN)

        self.butt = gpio.input(10)
        self.lcdOutput = lcd()
        self.musicController = music()

        self.inxex = [0,0]
        #TODO: Make the setOutput function check to see if it really needs to print out characters to the screen
        self.lastOutput = ["", ""]

        self.nextButtonPress = 0
        self.waitingForButton = True
