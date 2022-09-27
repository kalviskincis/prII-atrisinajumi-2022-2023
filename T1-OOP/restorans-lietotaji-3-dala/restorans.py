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