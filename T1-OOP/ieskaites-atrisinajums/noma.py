from datetime import datetime

class Noma:
    def __init__ (self, produkta_kategorija, produkta_nosaukums, tehniskie_raksturojumi, nomas_cena_diena, produkts_pieejams, nomnieka_vards, nomnieka_uzvards, nomnieka_pk, nomnieka_tel_nr, nomas_sakuma_datuma, nomas_beigu_datums):
        self.produkta_kategorija = produkta_kategorija
        self.produkta_nosaukums = produkta_nosaukums
        self.tehniskie_raksturojumi = tehniskie_raksturojumi
        self.nomas_cena_diena = nomas_cena_diena
        self.produkti_pieejami = produkts_pieejams
        self.nomnieka_vards = nomnieka_vards
        self.nomnieka_uzvards = nomnieka_uzvards
        self.nomnieka_pk = nomnieka_pk
        self.nomnieka_tel_nr = nomnieka_tel_nr
        self.nomas_sakuma_datums = nomas_sakuma_datuma
        self.nomas_beigu_datums = nomas_beigu_datums

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

    def produkta_info(self):
        return f"Produkta kategorija: {self.produkta_kategorija}\n produkta nosaukums: {self.produkta_nosaukums}\n tehniskie raksturojumi: {self.tehniskie_raksturojumi}\n nomas cena diena: {self.nomas_cena_diena}\n produkts pieejams: {self.produkti_pieejami}"

    def produkta_info_print(self):
        teksts = self.produkta_info()
        with open("produkta_info.txt", "w") as f:
            f.write(teksts)

    def nomnieka_info(self):
        return f"Nomnieka vards: {self.nomnieka_vards}\n nomnieka uzvards: {self.nomnieka_uzvards}\n nomnieka pk: {self.nomnieka_pk}\n nomnieka tel nr: {self.nomnieka_tel_nr}" 

    def nomnieka_info_print(self):
        teksts = self.nomnieka_info()
        with open("nomnieka_info.txt", "w") as f:
            f.write(teksts)
    
# tests = Noma("Zāģi", "BR15", "Stiprs", 7, "Jā", "Andris", "Andrissons", "112233-44556", "23456789", "2022-10-10", "2022-10-31")
# print(tests.nomas_atlikusais_laiks())
# print(tests.cena_kopa())
# print(tests.produkta_info())
# print(tests.nomnieka_info())
# tests.produkta_info_print()
# tests.nomnieka_info_print()
    

    

