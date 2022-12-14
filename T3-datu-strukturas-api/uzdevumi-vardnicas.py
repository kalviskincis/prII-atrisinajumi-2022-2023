1. uzdevums
atzimes = {10: "izcili", 9: "teicami"} # un pārējie vērtējumi
atzime = int(input("cik?"))
print(atzimes[atzime])

# 2. uzdevums
# klasesbiedru idejas
saraksts = [i for i in range(1, 21)]
print(saraksts)
kvadrati = [i**2 for i in saraksts]
print(kvadrati)
vardnica = {}
for i in range(20):
    vardnica[saraksts[i]] = kvadrati[i]
print(vardnica)


# "tradicionāli"

vardnica = {}
for sk in range(1, 21):
    vardnica[sk] = sk**2
print(vardnica)

# dictionary comprehension
vardnica_kv = {sk: sk**2 for sk in range(1, 21)}
print(vardnica_kv)

vardnica = {i for i in range(1,101)}
summas = sum(vardnica)
print(vardnica, summas)

# 3. uzdevums
# vienkārši
vardnica = {}
for i in range(1, 101):
    vardnica[i] = sum(range(1,i+1))
print(vardnica)

# ar directory comprehension
vards = {i: sum(range(1, i+1)) for i in range(1, 101)}
print(vards)



# 4. uzdevums
pirmskaitli = {1:2, 2:3, 3:5, 4:7, 5:11, 6:13, 7:17}

# v1
pirmskaitli_ekstra = {atslega: (vertiba, vertiba**2) for (atslega, vertiba) in pirmskaitli.items()}
print(pirmskaitli_ekstra)

#v2
pirmskaitli_ekstra_v2 = {i: (pirmskaitli[i], pirmskaitli[i]**2) for i in pirmskaitli}
print(pirmskaitli_ekstra_v2)

#V3
numurs = {}
for i in pirmskaitli:
    numurs[i] = (pirmskaitli[i], pirmskaitli[i]**2)
print(numurs)

# 5. uzdevums

#v1
tulkojums1 = {0: "nulle", 1: "viens", 2: "divi"}
tulkojums2 = {3: "trīs", 4: "četri", 5: "pieci"}
tulkojums3 = {6: "seši", 7: "septiņi", 8: "astoņi"}

tulkojums = {}
tulkojums.update(tulkojums1)
tulkojums.update(tulkojums2)
tulkojums.update(tulkojums3)
print(tulkojums)

#V2
visas = {** tulkojums1, ** tulkojums2, ** tulkojums3}
print(visas)