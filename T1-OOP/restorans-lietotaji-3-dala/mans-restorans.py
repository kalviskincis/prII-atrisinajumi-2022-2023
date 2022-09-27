# viens importēšanas veids
import restorans

lido = restorans.Restorans('Lido', 'latviešu virtuve')
print(lido.nosaukums)
print(lido.virtuves_veids)

# cits importēšanas veids
from restorans import Restorans

lido = Restorans('Lido', 'latviešu virtuve')
print(lido.nosaukums)
print(lido.virtuves_veids)

# līdzīgi kā pirmais, bet importējam ar īsāku nosaukumu
import restorans as r

lido = r.Restorans('Lido', 'latviešu virtuve')
print(lido.nosaukums)
print(lido.virtuves_veids)