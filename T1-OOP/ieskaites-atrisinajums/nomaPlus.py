from datetime import datetime
import json

class Noma:
    def __init__ (self, produkta_kategorija, produkta_nosaukums, tehniskie_raksturojumi, produkts_pieejams):
        self.produkta_kategorija = produkta_kategorija
        self.produkta_nosaukums = produkta_nosaukums
        self.tehniskie_raksturojumi = tehniskie_raksturojumi
        self.produkti_pieejami = produkts_pieejams

    def produkta_info(self):
        return f"Produkta kategorija: {self.produkta_kategorija}\n produkta nosaukums: {self.produkta_nosaukums}\n tehniskie raksturojumi: {self.tehniskie_raksturojumi}\n produkts pieejams: {self.produkti_pieejami}"

    def produkta_info_print(self):
        teksts = self.__dict__
        datiJSON = json.dumps(teksts, ensure_ascii=False)
        with open("produkta_apraksts.json", "w", encoding="utf-8") as f:
            f.write(datiJSON)

class Nomnieks:
    def __init__ (self, nomnieka_vards, nomnieka_uzvards, nomnieka_pk, nomnieka_tel_nr, nomas_sakuma_datuma, nomas_beigu_datums, nomas_cena_diena):
        self.nomnieka_vards = nomnieka_vards
        self.nomnieka_uzvards = nomnieka_uzvards
        self.nomnieka_pk = nomnieka_pk
        self.nomnieka_tel_nr = nomnieka_tel_nr
        self.nomas_sakuma_datums = nomas_sakuma_datuma
        self.nomas_beigu_datums = nomas_beigu_datums
        self.nomas_cena_diena = nomas_cena_diena

    def nomnieka_info(self):
        return f"Nomnieka vards: {self.nomnieka_vards}\n nomnieka uzvards: {self.nomnieka_uzvards}\n nomnieka pk: {self.nomnieka_pk}\n nomnieka tel nr: {self.nomnieka_tel_nr}" 

    def nomnieka_info_print(self):
        teksts = self.__dict__
        datiJSON = json.dumps(teksts, ensure_ascii=False)
        with open("nomnieka_apraksts.json", "w", encoding="utf-8") as f:
            f.write(datiJSON)

    def nomas_atlikusais_laiks(self):
        sodien = datetime.now()
        beigas = datetime.strptime(self.nomas_beigu_datums, '%Y-%m-%d')
        atlicis = (beigas - sodien).days
        return atlicis

    def cena_kopa(self):
        sakums = datetime.strptime(self.nomas_sakuma_datums, '%Y-%m-%d')
        beigas = datetime.strptime(self.nomas_beigu_datums, '%Y-%m-%d')
        kopa_dienas = (beigas - sakums).days
        jamaksa = kopa_dienas * self.nomas_cena_diena
        return jamaksa
    
testsPr = Noma("Zāģi", "BR15", "Stiprs", "Jā")
testsNom = Nomnieks("Andris", "Andrissons", "112233-44556", "23456789", "2022-10-10", "2022-10-31", 7)

print(testsNom.nomas_atlikusais_laiks())
print(testsNom.cena_kopa())
print(testsPr.produkta_info())
print(testsNom.nomnieka_info())
testsPr.produkta_info_print()
testsNom.nomnieka_info_print()
    

    

