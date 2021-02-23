import os

class test:
    def getSongs(self):

        if self.verbose:
            print( "Searching for songs...")
        for root, dirs, files in os.walk(self.path + "/songs"):
            for file in files:
                if ".mp3" in file:
                    self.songs.append( file )#os.path.join(root, file))
        if self.verbose:
            songCount = len(self.songs)
            if songCount == 0:
                print("No songs found.")
            elif songCount == 1:
                print("Found " + str(len(self.songs)) + " song.")
            else:
                print("Found " + str(len(self.songs)) + " songs.")

    def __init__(self):
        self.path = "/home/chesspro13"
        self.songs = []
        self.verbose = True

t = test()

t.getSongs()
