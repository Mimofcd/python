import random
class Track:
    def __init__(self,title,artist,duration):
        self.title=title
        self.artist=artist
        self.duration=duration

class Playlist:
    def __init__(self,title,filename):
        self.title=title
        self.filename=filename
        self.tracks=[]
        
    def load(self):
        self.tracks=[]
        print("Loading tracks from CSV file...")
        file=open(self.filename,"r")
        for line in file:
            fields=line.split(";")
            track=Track(fields[0],fields[1],int(fields[2]))
            self.tracks.append(track)
        file.close
    def save(self):
        print("Saving your playlist: ")
        file=open(self.filename,"w")
        for track in self.tracks:
            file.write(track.title+";"+track.artist+";"+str(track.duration)+";\n")
        file.close()
        print("Playlist saved")
    def enqueue(self,track):
        self.tracks.append(track)
    def getNoOfTracks(self):
        return len(self.tracks)
    def getTotalDuration(self):
        total=0
        for track in self.tracks:
            total=total+track.duration
        return total
    def shuffle(self):
        random.shuffle(self.tracks)
    def reset(self):
        self.tracks=[]
    def isEmpty(self):
        if len(self.tracks)==0:
            print("Playlist empty")
            return True
        else:
            print("Playlist not empty")
            return False
    def removeTrack(self,track):
        self.tracks.remove(track)   
    def view(self):
        print(self.title)
        trackNumber=1
        for track in self.tracks:
            print(str(trackNumber)+")"+track.title+" by "+track.artist+" - "+str(track.duration)+" s")
            trackNumber+=1