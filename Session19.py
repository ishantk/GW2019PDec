class Song:

    def __init__(self, title, artist, length, nextSong, prevSong):
        self.title = title
        self.artist = artist
        self.length = length
        self.nextSong = nextSong
        self.prevSong = prevSong

    def showSong(self):
        print(self.title,"|",self.artist,"|",self.length)

    def showNextSong(self):
        if self.nextSong is not None:
            self.nextSong.showSong()
        else:
            print(">> No Next Song Available")

    def showPrevSong(self):
        if self.prevSong is not None:
            self.prevSong.showSong()
        else:
            print(">> No Previous Song Available")

# Happy New Year
def addSongToEndOfPlayList(song):
    pass

def addSongToBeginningOfPlayList(song):
    pass

def addSongInBetweenPlayList(song1, song2):
    pass


def showPlayList(song):

    tempSong = song

    while tempSong.nextSong != song:
        tempSong.showSong()
        tempSong = tempSong.nextSong

    tempSong.showSong()

def showReversePlayList(song):

    tempSong = song

    while tempSong.prevSong != song:
        tempSong.showSong()
        tempSong = tempSong.prevSong

    tempSong.showSong()


s1 = Song("song1.mp3", "john", 5, None, None)

s2 = Song("song2.mp3", "fionna", 5.5, None, s1)
s1.nextSong = s2

s3 = Song("song3.mp3", "john", 7, None, s2)
s2.nextSong = s3

s4 = Song("song4.mp3", "Kim", 9, None, s3)
s3.nextSong = s4


s1.prevSong = s4
s4.nextSong = s1

# s1.showSong()
# s1.showPrevSong()
# s1.showNextSong()

showPlayList(s1)

print()

showReversePlayList(s4)
