#Alari Viilma
#1.11.22
#harjutus07
import math

def kuup(a):
    print(f"Kuubi ruumala on {a**3}")
def koonus(r,h):
    print(f"Koonuse ruumala on {round((math.pi*r**2)*h/3,2)}")
def silinder(k,l):
    print(f"Silindri ruumala on {(math.pi*k**2)*l}")

print("*************LEIAME RUUMALA*************")
loop = 1

while loop==1:
    print("Vali kujund \n1.Kuup \n2.Kera \n3.Koonus \n4.silinder")
    kujund = int(input("Liusa kujundi number 1-4: "))
    if kujund ==1:
        x = int(input("Sisesta kuubi külje pikkus: "))
        kuup(x)
    elif kujund==2:
        kera()
    elif kujund==3:
        r = int(input("Sisesta koonuse põhja raadius: "))
        h = int(input("Sisesta koonuse kõrgus: "))
        koonus(r,h)
    elif kujund==4:
        l = int(input("Sisesta silindri põhja raadius: "))
        k = int(input("Sisesta silindri kõrgus: "))
        silinder(k,l)
    else:
        print("*************\nPalun tee valik 1-4\n*************")
