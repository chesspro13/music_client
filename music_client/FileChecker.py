import os
# System opperates off of files. If the website creates a file, the client sees that and performs opperations depending on if a file is there.


class FileChecker:

    def checkPlay(self):
        if os.path.isfile(self.path + "/commands/play"):
            os.system("sudo rm " + self.path + "/commands/play")
            return True
        return False

    def checkPause(self):
        if os.path.isfile(self.path + "/commands/stop"):
            os.system("sudo rm " + self.path + "/commands/stop")
            return True
        return False

    def checkVolumeUp(self):
        if os.path.isfile(self.path + "/commands/volumeUp"):
            os.system("sudo rm " + self.path + "/commands/volumeUp")
            return True
        return False

    def checkVolumeDown(self):
        if os.path.isfile(self.path + "/commands/volumeDown"):
            os.system("sudo rm " + self.path + "/commands/volumeDown")
            return True
        return False

    # Depracated?
    def checkGetTime(self):
        if os.path.isfile(self.path + "/commands/getTime"):
            os.system("sudo rm " + self.path + "/commands/getTime");
            self.setCurPlayTime(self.music.getCurPlayTime())
            return True
        return False

    def setCurPlayTime(self, curPlayTime):
        f = open(self.path + "/commands/curTime", "w")
        s = f.write(str(curPlayTime))
        f.close()

    def setTotalPlayTime(self, totalPlayTime):
        f = open(self.path + "/commands/audioLength", "w")
        s = f.write(str(totalPlayTime))
        f.close()

    def getSongs(self):

        if self.verbose:
            print("Searching for songs...")
        for root, dirs, files in os.walk(self.path + "/songs"):
            for file in files:
                if ".mp3" in file:
                    self.songs.append(file) #os.path.join(root, file))
        if self.verbose:
            songCount = len(self.songs)
            if songCount == 0:
                print("No songs found.")
            elif songCount == 1:
                print("Found " + str(len(self.songs)) + " song.")
            else:
                print("Found " + str(len(self.songs)) + " songs.")

    def getDefaultSong(self):
        # TODO: Impliment!
        print("getDefaultSong() not implimented! Using default value of low.mp3")
        return "low.mp3"

    def checkOnPi(self):
        if os.path.isfile("/onPi"):
            return True
        else:
            return False

#    def init(self, path, music):
    def __init__(self):
        self.path = "/speaker"
        # self.music = music

        self.list_of_files = []