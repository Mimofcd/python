from functools import total_ordering
from hashlib import new
from re import T
from playlist import Track,Playlist

myPlaylist=Playlist("Pop Music","D:\\Phyton\\101computing\\mp3\\pop__music.csv")
myPlaylist.load()
newTrack=Track("Wonderwall","Oasis",255)
myPlaylist.enqueue(newTrack)
myPlaylist.view()
myPlaylist.isEmpty()
myPlaylist.removeTrack(myPlaylist.tracks[2])
myPlaylist.removeTrack(myPlaylist.tracks[5])
myPlaylist.removeTrack(myPlaylist.tracks[7])
myPlaylist.view()
noOfTracks=myPlaylist.getNoOfTracks()
print("This playlist have "+str(noOfTracks)+" tracks!")
totalDuration=myPlaylist.getTotalDuration()
print("This playlist lasts "+str(totalDuration)+ " seconds!")
myPlaylist.shuffle()
myPlaylist.view()
myPlaylist.reset()
myPlaylist.view()
myPlaylist.isEmpty()
myPlaylist.save()