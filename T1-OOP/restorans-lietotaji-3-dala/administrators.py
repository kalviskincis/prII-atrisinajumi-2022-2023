from lietotajs import Lietotajs

class Privilegijas():
    def __init__(self, privilegijas = []):
        self.privilegijas = ["pievienot lietotāju", "dzēst lietotāju", "bloķēt lietotāju"]

    def paradit_privilegijas(self):
        for privilegija in self.privilegijas:
            print(f"{privilegija}")

class Admin(Lietotajs):
    def __init__ (self, vards, uzvards, lietotajvards, epasts, pieteiksanos_skaits=0):
        super().__init__(vards, uzvards, lietotajvards, epasts, pieteiksanos_skaits)
        self.privilegijas = ["pievienot lietotāju", "dzēst lietotāju"] # šī rinda 7. uzdevumam
        self.privilegijas_citas = Privilegijas() # šī rinda 8. uzdevumam

    def paradit_privilegijas(self):
        print(self.privilegijas)