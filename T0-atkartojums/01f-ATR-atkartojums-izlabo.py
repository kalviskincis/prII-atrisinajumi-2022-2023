import random

def pirma():
# jāparāda uzrakstu "Programmēšana II"
    print("Programmēšana II")

def otra(atzime):
    # Jāparāda uzraksti "Labi", "Izcili" vai "cits vērtējums", atkarībā no parametrā iedotā skaitļa
    if atzime == 7:
        print("Labi")
    elif atzime == 10:
        print("Izcili")
    else:
        print("cits vērtējums")

def tresa():
    # Jāparāda stabiņā skaitļi no 1 līdz 10
    for i in range(1, 11):
        print(i)

def ceturta():
    # Jāparāda stabiņā uz leju masība mas ieraksti
    mas = [9, 6, 7, 3, 4, 10, 7]
    for viens in mas:
        print(viens)

def piekta():
    # Jāparāda nejaušu skaitli starp 0 un 1
    print(random.random())

def sesta(a, b):
    # jāparāda parametru a un b reizinājums
    print(a*b)

def septita():
    # jāizsauc funkcija pirma
    pirma()