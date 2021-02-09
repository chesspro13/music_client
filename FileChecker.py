import os

# System opperates off of files. If the website creates a file, the client sees that and performs opperations depending on if a file is there.

class FileChecker:

    def checkPlay(self):
        if os.path.isfile(self.path + "/commands/play"):
            os.system("sudo rm " + self.path + "commands/play")
            return True
        return False

    def checkPause(self):
        if os.path.isfile(self.path + "/commands/stop"):
            os.system("sudo rm " + self.path + "/commands/stop")
            return True
        return False

    def checkVolumeUp(self):
        if os.path.isfile(self.path + "/volumeUp"):
            os.system("sudo rm " + self.path + "/commands/volumeUp")
            return True
        return False

    def checkVolumeDown(self):
        if os.path.isfile(self.path + "commands/volumeDown"):
            os.system("sudo rm " + self.path + "/commands/volumeDown")
            return True
        return False

    def checkVolumeDown(self):
        if os.path.isfile(self.path + "/commands/getTime"):
            os.system("sudo rm " + self.path + "/commands/getTime");
            return True
        return False

    def setCurPlayTime(self, curPlayTime):
        f = open(self.path + "/commands/curTime", "w")
        s = f.write(str(curPlayTime))
        f.close()

    def setTotalPlayTime(self, totalPlayTime):
        f = open(self.path + "commands/audioLength", "w")
        s = f.write(str(totalPlayTime))
        f.close()

    def init(self, path):
        self.path = path
