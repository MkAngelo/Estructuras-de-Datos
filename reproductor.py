"""Reproductor de musica con Queue"""

from list_based_queue import ListQueue


class Player(ListQueue):
    def __init__(self):
        super().__init__()

    def add(self, song):
        self.enqueue(song)
    
    def play(self):
        try: 
            song = self.dequeue()
            if song:
                print(f'Playing - {song}')
        except:
            print('Your play list are empty')
    

        