import os


class test:


    def __init__(self):

        self.songs = {
            "Gamble Of My Thoughts",
            "Strings Of A Chance",
            "Admiring His Own",
            "Amused By His Soul",
            "Brave Kisses",
            "Super Show",
            "Babe, You And I Foreve",
            "oney, Take My Breath Awa",
            "He thinks I Won't Stop",
            "She said We're In Love",
            "Out Of Madness",
            "Era For Once",
            "Forget About Your Heart",
            "Change His Music",
            "Pretty Forever",
            "Sure Moves",
            "We're Crazy In Love",
            "I Need You",
            "He Likes You",
            "She heard We're In Love"

        }
        for i in self.songs:
            os.system("touch /speaker/songs/" + i.replace(" ","_") + ".mp3")


t = test()