#Alari Viilma
#11.10.22
#harjutus02
import math


km = 200
l = 30
vastus = l/(km/100)
print(vastus)





b =int(input("sisesta täisarv: "))
print("2ndsysmteemis:",bin(b))
print("16ndsysteemis:",hex(b))






#ajatesiendus
aeg =int(input("sisesta minutid: "))
tunnid = aeg // 60
minutid = aeg % 60
print("Vastus:",tunnid,":",minutid)





#hypotenuus
a,b = 16,9
c = round(math.sqrt(pow(a,2) + b**2),2)
print("Kolmnurga hüpo on:",c)




#rullujsud

kiirus = 29.9
aeg = 24
kaugus = round(kiirus/60*aeg,2)
print ("sportlane jõuab",kaugus,"km")






#pitsa hind
hind = 12.9
tip = 0.1
kogus = 3
summa =(hind+hind*tip)/kogus
print (kogus,"pitsa hind on", summa,"eurot")



#toote hind
hind = 36.75
ale = 0.4
kogus = 3
summa = round((hind-hind*ale)*3,2)
print(kogus,"toote summa on",summa,"eurot")


#kolmnurga ümbermõõt
a,b,c = 5,5,5
p = a + b + c
print("kolmnurga ümbermõõt on: ", p)