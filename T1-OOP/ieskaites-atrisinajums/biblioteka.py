from datetime import datetime

class Biblioteka:
    def __init__ (self, iespieddarba_kategorija, iespieddarba_nosaukums, iespieddarba_autors, izdevums_pieejams, lasitajs_vards, lasitajs_uzvards, izsniegsanas_datums, izsniegsanas_termins, atdosanas_datums):
        self.iespieddarba_kategorija = iespieddarba_kategorija
        self.iespieddarba_nosaukums = iespieddarba_nosaukums
        self.iespieddarba_autors = iespieddarba_autors
        self.izdevums_pieejams = izdevums_pieejams
        self.lasitajs_vards = lasitajs_vards
        self.lasitajs_uzvards = lasitajs_uzvards
        self.izsniegsanas_datums = izsniegsanas_datums
        self.izsniegsanas_termins = izsniegsanas_termins
        self.atdosanas_datums = atdosanas_datums

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
        teksts = self.iespieddarba_info()
        with open("izdevuma_apraksts.txt", "w", encoding="utf-8") as f:
            f.write(teksts)

    def lasitaja_info(self):
        return f"{self.lasitajs_vards}, {self.lasitajs_uzvards}"

    def lasitaja_info_print(self):
        teksts = self.lasitaja_info()
        with open("lasitaja_apraksts.txt", "w", encoding="utf-8") as f:
            f.write(teksts)

# g1 = Biblioteka("grāmata", "Astronomija", "Ilgonis Vilks", "Jā", "Anna", "Lasītāja", "10.10.2022", 5, "26.10.2022")
# print(g1.iespieddarba_info())
# print(g1.lasitaja_info())
# print(g1.atlikusais_laiks())
# print(g1.kavejuma_nauda())

# g1.iespieddarba_info_print()
# g1.lasitaja_info_print()

    
