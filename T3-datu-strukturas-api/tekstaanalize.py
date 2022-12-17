def analizet(datnes_nosaukums, garums):
    try:
        with open(datnes_nosaukums, "r", encoding="utf-8") as f:
            teksts = f.read()
            print(teksts)

            skaits = len(teksts)
            print(f"Simbolu skaits: {skaits}")

            pirmie_desmit = teksts[0:10]
            print(pirmie_desmit)

            print(teksts[0] + teksts[-1])

            fragments = teksts[0:garums]
            print(fragments)

    except FileNotFoundError:
        print(f"Datne {datnes_nosaukums} nav atrasta.")

    except TypeError:
        print("Kāds no ievades datiem nav korekts")

    finally:
        print("Viss izdarīts, beigas")

def pirmarinda(datnes_nosaukums):
        with open(datnes_nosaukums, "r", encoding="utf-8") as f:
        teksts = f.read()
        sadalits = teksts.splitlines()
        print(teksts.splitlines()[0])

        teksts = f.readline()
        print(teksts)

        teksts2 = f.readline()
        print(teksts2)


# analizet("balta-pasaka.txt", 20)
pirmarinda("zakisupirtina.txt")
