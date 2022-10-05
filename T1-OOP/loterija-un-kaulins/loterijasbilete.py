import random

simboli = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D")

class Bilete:
    def izveidot_bileti():
        bilete = []
        for i in range(4):
            sim = random.choice(simboli)
            bilete.append(sim)
        return bilete