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