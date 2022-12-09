# 1. uzdevums

menesi = ("jan", "feb", "mar", "apr", "mai", "jūn", "jūl", "aug", "sep", "okt", "nov", "dec")
mans = menesi.index("apr")
print(menesi[mans], mans)


# 2. uzdevums
t=("a", "b", "c", "d")
for i in range(len(t)):
    print(t[len(t)-1-i])

for i in range(len(t)-1, -1, -1):
    print(t[i])

# 3. uzdevums
ts=( (4,7), (9,2) )
print(sum(ts[0]+ts[1]))