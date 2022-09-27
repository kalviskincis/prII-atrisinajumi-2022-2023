class Lietotajs:
    def __init__ (self, vards, uzvards, lietotajvards, epasts, pieteiksanos_skaits=0):
        self.vards = vards
        self.uzvards = uzvards 
        self.lietotajvards = lietotajvards
        self.epasts = epasts
        self.pieteiksanos_skaits = pieteiksanos_skaits

    def lietotaja_apraksts(self):
        print(f"Lietotājs {self.vards} {self.uzvards} ar lietotājvārdu {self.lietotajvards} un e-pastu {self.epasts}")

    def sasveicinies(self):
        print(f"Sveicināti, {self.vards}!")
    
    def palieninat_pieteiksanos_skaitu(self):
        self.pieteiksanos_skaits += 1

    def atiestatit_pieteiksanos_skaitu(self):
        self.pieteiksanos_skaits = 0

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

ansis = Lietotajs('Ansis', 'Krauklis', 'ansis', 'akrauklis@organizacija.lv')
ansis.lietotaja_apraksts()
ansis.sasveicinies()

amanda = Lietotajs('Amanda', 'Zīle', 'amanda', 'azile@organizacija.lv')
amanda.lietotaja_apraksts()
amanda.sasveicinies()

amanda.palieninat_pieteiksanos_skaitu()
amanda.palieninat_pieteiksanos_skaitu()
amanda.palieninat_pieteiksanos_skaitu()
print(amanda.pieteiksanos_skaits)
amanda.atiestatit_pieteiksanos_skaitu()
print(amanda.pieteiksanos_skaits)

mickey = Admin("Mickey", "Mouse", "mickey", "mmouse@organizacija.lv")
mickey.paradit_privilegijas() # šī rinda 7. uzdevumam
mickey.privilegijas_citas.paradit_privilegijas() # šī rinda 8. uzdevumam