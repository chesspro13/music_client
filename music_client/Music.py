from subprocess import call
import FileChecker
import vlc


class Music:

    def play(self):
        self.musicPlayer.set_pause(0)

    def pause(self):
        self.musicPlayer.set_pause(1)

    def volumeUp(self):
        if self.volume < 100:
            self.volume += 10

            # Amixer is not a viable option for running in a container since I cannot access the host system!
            # Need to determine if writing a standalone script for the pi to monitor volume change files is worth it...
            call( ["amixer", "-D", "pulse", "sset", "Master",str(self.volume)+"%"] )


    def volumeDown(self):
        if self.volume > 0:
            self.volume -= 10
            
            # Amixer is not a viable option for running in a container since I cannot access the host system!
            # Need to determine if writing a standalone script for the pi to monitor volume change files is worth it...
            call( ["amixer", "-D", "pulse", "sset", "Master",str(self.volume)+"%"] )

    def toggle(self):

        if self.playing:
            self.musicPlayer.set_pause(1)
            self.playing = False
        else:
            self.musicPlayer.set_pause(0)
            self.playing = True
        print("Music toggled.")

    def setCurPlayTime(self):
        self.fc.setCurPlayTime(self.musicPlayer.get_time())

    def getCurPlayTime(self):
        return self.musicPlayer.get_time()

    def getTotalPlayTime(self):
        return self.musicPlayer.get_length()

    def getSongName(self):
        return self.songName

    def changeSong(self, song):
        self.songName = song
        self.musicPlayer = vlc.MediaPlayer(self.path + "/songs/" + self.songName)
        self.musicPlayer.play()
        self.playing = True

    def setPath(self, path):
        self.path = path

    def __init__(self):
        self.fc = FileChecker.FileChecker()
        self.playing = False

        # This one is for computers
        # DEPRICATED! Keeping until safe to remove
        #            self.musicPlayer = vlc.MediaPlayer("/home/pi/songs/low.mp3")
        
        self.changeSong(self.fc.getDefaultSong())
        self.volume = 100

        # Amixer is not a viable option for running in a container since I cannot access the host system
        # Need to determine if writing a standalone script for the pi to monitor volume change files is worth it...
        call(["amixer", "-D", "pulse", "set", "Master", str(self.volume)+"%"])
