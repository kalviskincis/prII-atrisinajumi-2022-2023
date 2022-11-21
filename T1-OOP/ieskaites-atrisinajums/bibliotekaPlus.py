from datetime import datetime
import json

# class Biblioteka:
#     def __init__ (self, iespieddarba_kategorija, iespieddarba_nosaukums, iespieddarba_autors, izdevums_pieejams, izsniegsanas_datums, izsniegsanas_termins, atdosanas_datums):
#         self.iespieddarba_kategorija = iespieddarba_kategorija
#         self.iespieddarba_nosaukums = iespieddarba_nosaukums
#         self.iespieddarba_autors = iespieddarba_autors
#         self.izdevums_pieejams = izdevums_pieejams
#         self.izsniegsanas_datums = izsniegsanas_datums
#         self.izsniegsanas_termins = izsniegsanas_termins
#         self.atdosanas_datums = atdosanas_datums

class Biblioteka:
    def __init__(self, vardnica):
        for key in vardnica:
            setattr(self, key, vardnica[key])


    def atlikusais_laiks(self):
        tagad = datetime.now()
        izsniegts = datetime.strptime(self.izsniegsanas_datums, "%d.%m.%Y")
        cik_ilgi_izsniegts = (tagad - izsniegts).days
        cik_atlicis = self.izsniegsanas_termins - cik_ilgi_izsniegts
        return cik_atlicis

    def kavejuma_nauda(self):
        atdots = datetime.strptime(self.atdosanas_datums, "%d.%m.%Y")
        izsniegts = datetime.strptime(self.izsniegsanas_datums, "%d.%m.%Y")
        cik_ilgi_izsniegts = (atdots - izsniegts).days
        if cik_ilgi_izsniegts > self.izsniegsanas_termins:
            kavejuma_nauda = (cik_ilgi_izsniegts - self.izsniegsanas_termins) * 0.50
            return kavejuma_nauda
        else:
            return 0

    def iespieddarba_info(self):
        return f"{self.iespieddarba_kategorija}, {self.iespieddarba_nosaukums}, {self.iespieddarba_autors}"

    def iespieddarba_info_print(self):
        teksts = self.__dict__
        datiJSON = json.dumps(teksts, ensure_ascii=False)
        with open("izdevuma_apraksts.json", "w", encoding="utf-8") as f:
            f.write(datiJSON)

class Lasitajs:
    def __init__ (self, lasitajs_vards, lasitajs_uzvards):
        self.lasitajs_vards = lasitajs_vards
        self.lasitajs_uzvards = lasitajs_uzvards

    def lasitaja_info(self):
        return f"{self.lasitajs_vards}, {self.lasitajs_uzvards}"

    def lasitaja_info_print(self):
        teksts = self.__dict__
        datiJSON = json.dumps(teksts, ensure_ascii=False)
        with open("lasitaja_apraksts.json", "w", encoding="utf-8") as f:
            f.write(datiJSON)

with open("izdevuma_apraksts.json", "r", encoding="utf-8") as f:
    izdevuma_apraksts = json.load(f)

g1 = Biblioteka(izdevuma_apraksts)
print(g1.__dict__)
print(g1.iespieddarba_info())


# g1 = Biblioteka("grāmata", "Astronomija", "Ilgonis Vilks", "Jā", "10.10.2022", 5, "26.10.2022")
# print(g1.iespieddarba_info())
# print(g1.atlikusais_laiks())
# print(g1.kavejuma_nauda())
# g1.iespieddarba_info_print()

# l1 = Lasitajs("Jānis", "Bērziņš")
# print(l1.lasitaja_info())
# l1.lasitaja_info_print()

    
