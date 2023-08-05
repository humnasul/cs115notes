from functools import * 
class Player:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.instruments = []

    def __str__(self):
        '''The artist and their instruments'''
        return "Artist "+self.name + " plays "+ ",".join(self.instruments)

    def copy(self):
        p = Player(self.name, self.genre)
        p.instruments = list(self.instruments)
        return p

    def addInst(self, instrument):
        self.instruments.append(instrument)

    def __eq__(self, other):
        '''Whether self and other have same name and genre and play the same instruments'''
        if self.name != other.name or self.genre != other.genre:
            return False
        else:
            if len(self.instruments) != len(other.instruments):
                return False
            else:
                sortedSelf = sorted(self.instruments)
                sortedOther = sorted(other.instruments)
                instEqual = reduce(lambda x, y : x and y, map(lambda p, q: p == q, sortedSelf, sortedOther), True)
                '''
                instEqual = True
                for i in range(len(sortedSelf)):
                    if sortedSelf[i].lower() != sortedOther[i].lower():
                        instEqual = False
                        break
                '''
                return instEqual

Meshell = Player("Ndegeocello", "rap")
Meshell.addInst("bass")
M2 = Meshell.copy()
M2.addInst("piano")
print(Meshell)

p0 = Player("Attila Duck", "jazz")
p0.addInst("kazoo")
p0.addInst("guitar")
p1 = Player("Attila Duck", "jazz")
p1.addInst("guitar")
p1.addInst("kazoo")
print(p0 == p1)
