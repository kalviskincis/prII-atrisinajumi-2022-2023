import json
from datetime import datetime

class Lietotajs:
    def __init__ (self, vards, uzvards, lietotajvards, epasts, dzimsanas_datums, pieteiksanos_skaits=0):
        self.vards = vards
        self.uzvards = uzvards 
        self.lietotajvards = lietotajvards
        self.epasts = epasts
        self.dzimsanas_datums = dzimsanas_datums
        self.pieteiksanos_skaits = pieteiksanos_skaits

    def lietotaja_apraksts(self):
        # print(f"Lietotājs {self.vards} {self.uzvards} ar lietotājvārdu {self.lietotajvards} un e-pastu {self.epasts}")
        dzd = self.nakama_dzimsanas_diena()
        return f"Lietotājs: {self.vards} {self.uzvards}\nlietotājvārds: {self.lietotajvards},\ne-pasts: {self.epasts}.\n{dzd}"

    def nakama_dzimsanas_diena(self):
        dzimsanas_diena = datetime.strptime(self.dzimsanas_datums, "%Y-%m-%d")
        sodien = datetime.now()
        if sodien.month == dzimsanas_diena.month and sodien.day == dzimsanas_diena.day:
            pazinojums = f"Daudz laimes, {self.vards}"
        elif sodien.month <= dzimsanas_diena.month:
            nakama_dz_d = datetime(sodien.year, dzimsanas_diena.month, dzimsanas_diena.day)
            dienas_lidz_dzd = (nakama_dz_d - sodien).days
            pazinojums = f"Līdz dzimšanas dienai {dienas_lidz_dzd} dienas"
        else:
            nakama_dz_d = datetime(sodien.year+1, dzimsanas_diena.month, dzimsanas_diena.day)
            dienas_lidz_dzd = (nakama_dz_d - sodien).days
            pazinojums = f"Līdz dzimšanas dienai {dienas_lidz_dzd} dienas"
        return pazinojums



    def sasveicinies(self):
        print(f"Sveicināti, {self.vards}!")
    
    def palieninat_pieteiksanos_skaitu(self):
        self.pieteiksanos_skaits += 1

    def atiestatit_pieteiksanos_skaitu(self):
        self.pieteiksanos_skaits = 0

    def saglabat_txt(self):
        dati = self.lietotaja_apraksts()
        with open("lietotajs.txt", "w", encoding="utf-8") as datne:
            datne.write(dati)

    def saglabat_json(self):
        dati = self.__dict__
        datiJSON = json.dumps(dati, ensure_ascii=False)
        with open("lietotajs.json", "w", encoding="utf-8") as datne:
            datne.write(datiJSON)