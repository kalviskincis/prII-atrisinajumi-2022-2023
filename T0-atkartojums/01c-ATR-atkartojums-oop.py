# Izveido konstruktoru klasei Suns
# Klasei jābūt ar vienu īpašību vards

class Suns:
    def __init__ (self, vards):
        self.vards = vards

    def est(self):
        print("Suns ēd")

    def skriet(self):
        print(f"{self.vards} skrien")


# konstruktorā izveido šādas darbības (metodes)
# est –– tai jāparāda teikums, ka suns ēd.
# skriet – tai jāparāda teikums, ka suns skrien, notiekti izmantojot arī suņa vārdu

# izveido divus klases Suns objektus s1 un s2 un tiem izsauc abas metodes.

# piemēram,

s1 = Suns("Reksis")
s1.est() # --- sagaidāmā izvade "Suns ēd"
s1.skriet() # --- sagaidāmā izvade "Reksis skrien"

s2 = Suns("Breksis")
s2.est()
s2.skriet()