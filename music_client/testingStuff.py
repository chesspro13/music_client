import os


class test:

    def getConfig(self, lookingFor):
        f = open("config/general_config.conf", "r")
        d = f.read()
        if d == lookingFor:
            return d.split("__")[2]


t = test()

t.getConfig("working_directory")