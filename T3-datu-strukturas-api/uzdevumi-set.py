# 2. uzdevums
para_sk = [i for i in range(2, 101, 2)]
para_sk_kopa = set(para_sk)
print(para_sk_kopa)

# vai arī
para_sk_kopa2 = {i for i in range(2, 101, 2)}
print(para_sk_kopa2)

# vai ar ierastiem paņēmieniem (līdzīgi kā append priekš list)
para_sk_kopa = set()
for i in range(2, 101, 2):
    para_sk_kopa.add(i)
print(para_sk_kopa)

# 3. uzdevums
x1 = 0
x2 = 1
skaitlu_virkne = [x1, x2]
for i in range(20):
    x = 2 * skaitlu_virkne[i+1] + skaitlu_virkne[i]
    skaitlu_virkne.append(x)
cik_nepari = len([sk for sk in skaitlu_virkne if sk%2==1])

print(skaitlu_virkne)
print(cik_nepari)

# vai arī, lai izmantotu datu tipa set pieejamās metodes
x1 = 0
x2 = 1
virkne = {x1, x2}
for i in range(20):
    xi = 2*x2 + x1
    virkne.add(xi)
    x1, x2 = x2, xi
print(virkne)


# 4. uzdevums

kopa = {"a", "c", "e"}
burts = input("burts: ")
if burts in kopa:
    kopa.discard(burts)
else:
    kopa.add(burts)
print(kopa)