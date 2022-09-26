a = 21
b = 7

# Nodefinē funkcju pirma() bez parametriem
# Funkcijai jāparāda a un b summa
def pirma():
    print(a+b)

# Nodefinē funkciju otra() ar diviem parametriem c un d
# Funkcijai jāatgriež abu parametru starpība --- return
def otra(c, d):
    return c+d


# Izsauc funkciju pirma()
# Izsauc funkciju otra() ar a un b kā parametriem
# Izsauc funkciju otra() ar diviem Tevis izvēlētiem skaitļiem kā parametriem
pirma()
otra(a, b)
otra(4, 5)


# Izveido funkciju tresa() bez parametriem
# tai jāizsauc funkcija otra() ar diviem Tevis izvēlētiem skaitļiem kā parametriem un rezultāts jāsaglabā mainīgajā e
# Mainīgā e vērtība jāparāda
def tresa():
    e = otra(10, 20)
    print(e)