import time
import winsound

class Note:
    def __init__(self):
        self._note = {'pause':0, 'c':1, 'c#':2, 'd':3, 'd#':4, 'e':5, 'f':6, 'f#':7, 'g':8, 'g#':9, 'a':10, 'a#':11, 'b':12}
        self._beat = {'whole':800, 'half':400, 'quarter':200, 'eigth':100, 'sixteenth':50, 'dotted_eigth':150, 'triplet':60}
        self._sleep = 0.15

    def beep():
        while True:
            winsound.Beep(100, 100)

    def play(self, octave, note, beat):
        note = self._note[note]
        beat = self._beat[beat]

        # Calculate C for the provided octave
        frequency = 32.7032 * (2**octave)

        # Calculate the frequency of the given note
        frequency *= 1.059463094**note
    
        # Beep it up
        winsound.Beep(int(frequency), beat)

        # Delay after the beep so it doesn't all run together
        time.sleep(self._sleep)

class Song:
    def __init__(self):
        self._note = []
        self._beat = []
        self._sleep = 0.15

    def set_note(self, n):
        self._note.append(n)

    def set_beat(self, b):
        self._beat.append(b)

    def get_note(self):
        return self._note

    def get_beat(self):
        return self._beat

def HBD(n):
    octave = 3
    note = ['g', 'g', 'a', 'g', 'c', 'b', 'g', 'g', 'a', 'g', 'd', 'c', 'g', 'g', 'g', 'e', 'c', 'b', 'a', 'f', 'f', 'e', 'c', 'd', 'c']
    beat = ['quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter']
    for k in range(0, len(note)):
        n.play(octave, note[k], beat[k])
    
def mission_impossible(n):
    oct = 3
    n.play(oct, "g", "half")
    n.play(oct, "g", "half")
    n.play(oct+1, "a#", "quarter")
    n.play(oct+1, "c", "quarter")
    n.play(oct, "g", "half")
    n.play(oct, "g", "half")
    n.play(oct, "f", "quarter")
    n.play(oct,  "f#", "quarter")
    n.play(oct, "g", "half")
    n.play(oct, "g", "half")
    n.play(oct+1, "a#", "quarter")
    n.play(oct+1, "c", "quarter")
    n.play(oct, "g", "half")
    n.play(oct, "g", "half")
    n.play(oct, "f", "quarter")
    n.play(oct,  "f#", "quarter")

def main():
    n = Note()    
    HBD(n)
    
    #mission_impossible(n)
    #n.play()
    #mission_impossible()    
    #time.sleep(.4)
        
if __name__ == '__main__':    
    main()
