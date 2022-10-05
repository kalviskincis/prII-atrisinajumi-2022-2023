import random

simboli = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D")

def uzvarejusi_bilete():
    bilete = []
    for i in range(4):
        sim = random.choice(simboli)
        bilete.append(sim)
    return bilete

mana_bilete = uzvarejusi_bilete()
cik = 0
uzvara = False

#for i in range(1000000):
while not uzvara:
    if uzvarejusi_bilete() == mana_bilete:
        print("Uzvarēji!")
        print(f"Tam vajadzēja {cik+1} mēģinājumus.")
        uzvara = True
        break
    else:
        cik += 1
