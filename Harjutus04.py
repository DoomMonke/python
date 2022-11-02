#Alari Viilma
#17.10.22
#harjutus04
import random

#pank
konto = 10000
intress = 0.05
periood = 5

for i in range(1,periood+1):
    print(f"{i} {round(konto,2)} {round(konto*intress,2)} {konto+konto*intress}")
    konto = konto+konto*intress 
print(f"Konto seis: {round(konto,2)}")
print(f"Kasum: {round(konto-10000,2)}")




print()

#arvamismäng
"""
loop = 1
skoor = 0
while loop==1:
    suvarv = random.randint(1,10)
    print(suvarv)
    for i in range(3):
        valik = int(input("vali arv 1-10: "))
        if valik ==suvarv:
            print("WINNER!")
            skoor+=1
            break
        else:
            print("WRONG!")
    loop=int(input("Veel (1/0)? "))
print("GAME OVER")
print(f"Skoor {skoor}")
"""






"""
#korrutus tabel
for i in range (1,11):
    for j in range(1,2):
        print("{0:>3}".format(j*i) , end= " ")
    print()

"""
"""
#loto
for i in range (5):
    suv = random.randint(0,9)
    print(suv, end="")

"""
"""


#tsükkel
arv=5
for i in range (5):
    print("* " * arv)
    arv -=1
    
arv=5
for i in range (5):
    print("* " * arv)
    arv +=1


nr = 5
for i in range(nr):
    print("* " * nr)

#jalgpall

vanus = 17
sugu = "n"

if vanus>=16 and vanus<=18 and sugu=="m":
    print("sobib meeskonda")
else:
    print("ei sobi")


"""
"""
#myyk
hind = 20
if hind<=10:
    ale = 0.1
else:
    ale = 0.2

print (f"Summa: {hind-hind*ale}€")

"""

"""

#juubel

aasta = "11.03.2007"
p,k,a = aasta.split(".")
vanus=2022-int(a)
if vanus%5 ==0: 
    print("juubel")
else:
    print("ei ole juubel")


"""

"""
#Matemaatika
nr1,nr2 = 8,6
tehe = input("Vali tehe (* / + -):")

if tehe=="*":
    vastus = nr1 * nr2
elif tehe=="/":
    vastus = nr1 / nr2
elif tehe=="+":
    vastus = nr1 + nr2
elif tehe=="-":
    vastus = nr1 - nr2


else:
    vastus:"N/A"


print(f"{nr1}{tehe}{nr2}={vastus}")
print("_______________________")



#kas on ruut
a =int(input("Sisesta külg 1: "))
b= int(input("Sisesta külg 2: "))

if a==b:
    print(f"{a} ja {b} moodustavad ruudu")
else:
    print(f"{a} ja {b} moodustavad ristkülik")
"""