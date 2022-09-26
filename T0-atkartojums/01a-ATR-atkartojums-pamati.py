a = int(input("Ieraksti vienu skaitli"))
b = int(input("Ieraksti citu skaitli"))

# turpini programmu, lai tā parādītu mainīgo a un b summu, reizinājumu un dalījuma atlikumu
# vismaz vienai no rindām jābūt noformētai kā pilnam teikumam --- print(), print(f'')
print(a+b)
print(a*b)
print(f'Atlikums no {a} un {b} dalījuma ir {a%b}')



# maini 1. un 2. rindas, lai mainīgo vērtības tiktu prasītas lietotājam --- input()

# Parādi stabiņā uz leju skaitļus no 1 līdz 5 ieskaitot --- for
for i in range(1, 6):
    print(i)

klases = ["12.a", "12.b", "12.c"]
# Parādi stabiņā uz leju masīva klases visus ierakstus
for viena in klases:
    print(viena)

# Parādi no masīva klases tikai ierakstu ar vērtību 12.a --- []
print(klases[0])

atbilde = input("Uzraksti slepenu vārdu")
# Noņem komentāra zīmi iepriekšējai rindai
# Ja, iedarbinot programmu, ievadītais vārds ir "nē", parādi ekrānā tekstu "Slepenais netika uzrakstīts"
# Visos citos gadījumos jāparāda teksts "Slepenais vārds ir" kopā ar ievadīto vārdu
# Papilduzdevums: programma parāda tekstu "Slepenais vārds ir" un tik zvaigznītes, cik garš ir lietotāja ievadītais vārds
if atbilde == "nē":
    print("Slepenais netika uzrakstīts")
else:
    print(f"Slepenais ir {atbilde}")