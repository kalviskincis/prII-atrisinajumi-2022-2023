def veido_pirmskaitlus(cik):
    pirmskaitli = [1]
    for i in range(2, cik):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            pirmskaitli.append(i)
    return pirmskaitli



def uzd1():
    saraksts = [i for i in range(1, 11)]
    print(saraksts)

    kvadrati = [i**2 for i in saraksts]

    kvadrati = []
    for katrs in saraksts:
        kvadrati.append(katrs**2)

    print(kvadrati)
    saraksts.extend(kvadrati)
    print(saraksts)
    return saraksts

def uzd2un3(saraksts):
    print(max(saraksts))
    print(min(saraksts))
    print(sum(saraksts))

def uzd4():
    fibo = []
    f1 = 1
    f2 = 1
    fibo = [f1, f2]
    for i in range(8):
        f2, f1 = f1+f2, f2
        fibo.append(f2)
    return fibo

def uzd5():
    pilsetas = ["Ape", "Daugavpils", "Kuldīga", "Baldone", "Valdemārpils"]
    garumi = [len(katra_pilseta) for katra_pilseta in pilsetas]
    lielakais_garums_nr = garumi.index(max(garumi))
    print(pilsetas[lielakais_garums_nr])

def uzd6():
    saraksts1 = [1, 2, 3]
    saraksts2 = [4, 5, 6]
    saraksts3 = saraksts1 + saraksts2
    return saraksts3

def uzd7():
    pirmskaitli = veido_pirmskaitlus(100)
    saraksts = [i for i in range(1, 101)]

    for viens_pirmskaitlis in pirmskaitli:
        if viens_pirmskaitlis in saraksts:
            saraksts.remove(viens_pirmskaitlis)

    return saraksts

def uzd8():
    saraksts  = uzd1()
    saraksts_set = set(saraksts)
    saraksts_gatavs = list(saraksts_set)
    saraksts_gatavs.sort()
    return saraksts_gatavs



uzd1_rezult= uzd1()
uzd2un3(uzd1_rezult)

fibo_virkne = uzd4()
print(fibo_virkne)

uzd5()

uzd6_rezult = uzd6()
print(uzd6_rezult)

uzd7_rezult = uzd7()
print(uzd7_rezult)

uzd8_rezult = uzd8()
print(uzd8_rezult)
