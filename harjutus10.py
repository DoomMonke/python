#Alari Viilma
#2.11.22
#harjutus10


#Ip address 

import re

fh = open('tekst.txt')
for line in fh:
    if re.search('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', line):
         print(line,end='')


print("-------------------------------------------------")

#Korralikud paroolid
import re

fh = open('tekst.txt')
for line in fh:
    if re.search('^[A-Za-z0-9]+[A-Z]{2}', line):
         print(line,end='')


