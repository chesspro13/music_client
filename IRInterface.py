from owainm713_IR_scripts.IRModule import IRRemote
import RPi.GPIO as GPIO
import FileChecker
import time


class IRInterface:
    def remote_callback(self, code):

        # Codes listed below are for the
        # Sparkfun 9 button remote

        #   print("Code: " + str(code))

        #   if code == 16753245:
        if code == 0xFFA25D:
            print('Power Button')
            return 'Power Button'
        elif code == 0xFFE21D:
            print( 'Menu Button')
            return 'Menu Button'
        elif code == 0xFF22DD:
            print( 'Testing')
            return 'Testing'
        elif code == 0xFF02FD:
            self.music.volumeUp()
            return 'Volume Up'
        elif code == 0xFFC23D:
            print('Restart')
            return 'Restart'
        elif code == 0xFFE01F:
            print('Back')
            return 'Back'
        elif code == 0xFFA857:
            self.music.toggle()
            return 'Play'
        elif code == 0xFF906F:
            print('Forward')
            return 'Forward'
        elif code == 0xFF9867:
            self.music.volumeDown()
            return 'Volume Down'

        #   else:
        #       print('.')  # unknown code

        return

    def init(self, irPin, fc, music):
        self.ir = IRRemote(callback='DECODE')
        self.music = music

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)      # uses numbering outside circles
        GPIO.setup(irPin, GPIO.IN)   # set irPin to input
        GPIO.add_event_detect(irPin, GPIO.BOTH, callback=self.ir.pWidth)

        self.fc = fc

        try:
            time.sleep(5)

            self.ir.set_verbose(False)
            self.ir.set_repeat( False )
            self.ir.set_callback(self.remote_callback)

            # This is where you could do other stuff
            # Blink a light, turn a motor, run a webserver
            # count sheep or mine bitcoin

            while True:
                time.sleep(1)

        except:
            print('Removing callback and cleaning up GPIO')
            self.ir.remove_callback()
            GPIO.cleanup(irPin)
