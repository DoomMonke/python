#Alari Viilma
#1.11.22
#harjutus07
import locale
import datetime

#Tänane kuupäev
aeg = datetime.datetime.now()
print(aeg.strftime("%d. %B %Y"))


#Eesti kuupäevad
locale.setlocale(locale.LC_ALL, "et_EE")
aeg = datetime.datetime.now()
print(aeg.strftime("%d. %B %Y"))




#eraldamine isiku koodist
ik="50610200246"
sp = datetime.date(int("20"+ik[1:3]), int(ik[3:5]), int(ik[5:7]))
print(sp)
print(aeg.year-sp.year - ((aeg.month, aeg.day < (sp.month,sp.day)))



