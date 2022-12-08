import random


class Kaulins:
    def __init__ (self, skaldnes = 6):
        self.skaldnes = skaldnes
    
    def mest_kaulinu(self):
        return random.randrange(1, self.skaldnes+1) 

k6 = Kaulins()
rezulati = []
for i in range(10):
    rezulati.append(k6.mest_kaulinu())
print(rezulati)

k10 = Kaulins(10)
rezulati = []
for i in range(10):
    rezulati.append(k10.mest_kaulinu())
print(rezulati)

k20 = Kaulins(20)
rezulati = []
for i in range(10):
    rezulati.append(k20.mest_kaulinu())
print(rezulati) 