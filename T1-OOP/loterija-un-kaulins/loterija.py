from loterijasbilete import Bilete

mana_bilete = Bilete.izveidot_bileti()
uzvarejusi_bilete = []
cik = 0

print(f'Mana bilete: {mana_bilete}')

for i in range(1000000):
    uzvarejusi_bilete = Bilete.izveidot_bileti()
    if uzvarejusi_bilete == mana_bilete:
        print("Uzvarēji!")
        print(f"Tam vajadzēja {cik} mēģinājumus.")
        break
    else:
        cik += 1

