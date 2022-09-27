from cgi import print_environ_usage


class Restorans():

    def __init__(self, nosaukums, virtuves_veids, apkalpoto_skaits = 0):
        self.nosaukums = nosaukums.title()
        self.virtuves_veids = virtuves_veids
        self.apkalpoto_skaits = apkalpoto_skaits

    def restorana_apraksts(self):
        teksts = f"{self.nosaukums} ir lieliska {self.virtuves_veids}."
        print(f"{teksts}")

    def restorans_atverts(self):
        teksts = f"{self.nosaukums} ir atvērts."
        print(f"{teksts}")

    def iestatit_apkalpoto_skaits(self, apkalpoto_skaits):
        self.apkalpoto_skaits = apkalpoto_skaits

    def palielinat_apkalpoto_skaitu(self, skaits):
        self.apkalpoto_skaits += skaits

class SaldejumaKiosks(Restorans):
    def __init__(self, nosaukums, virtuves_veids, apkalpoto_skaits = 0, garsas = []):
        super().__init__(nosaukums, virtuves_veids, apkalpoto_skaits)
        self.garsas = garsas

    def paradit_garsas(self):
        for garsa in self.garsas:
            print(f"{garsa}")

lido = Restorans('Lido', 'latviešu virtuve')
print(lido.nosaukums)
print(lido.virtuves_veids)

lido.restorana_apraksts()
lido.restorans_atverts()

pica = Restorans('Lulū', 'pica')
pica.restorana_apraksts()

asia = Restorans('Nice Asian', 'Āzijas virtuve')
asia.restorana_apraksts()

print(lido.apkalpoto_skaits)
lido.iestatit_apkalpoto_skaits(10)
print(lido.apkalpoto_skaits)
lido.palielinat_apkalpoto_skaitu(5)
print(lido.apkalpoto_skaits)

pingvins = SaldejumaKiosks("Pingvīns", "saldējumi", 5, ["plombīra", "šokolādes", "pīlādžu"])
pingvins.restorana_apraksts()
pingvins.paradit_garsas()