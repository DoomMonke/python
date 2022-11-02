#Alari Viilma
#17.10.22
#harjutus03

#mis asi on palindroom

def isPalindrome(palindrome):
    return palindrome == palindrome[::-1]
 

palindrome = "tere"
answer = isPalindrome(palindrome)
if answer:
    
    print("Yes")
else:
    print("No")




#tundide ajad
Algus = "8:30"
Lõpp = "14:15"

hh1,mm1= Algus.split(':') #tükeldan teksti
minutid1 = int(hh1)*60+int(mm1)#teisendan minutiteks
hh2,mm2= Lõpp.split(':')
minutid2 = int(hh2)*60+int(mm2)
minutid = minutid2-minutid1 #ajaahe
hh = minutid//60
mm = minutid%60

print(f"Ajaline vahe on {hh}:{mm}")


#Emaili kontroll true/false
Email = input("Sisesta email kontrollmiseks: ")
print("@" in Email)






#vandumine - teksi asendamine
v = input("Vannu siia 'kurat küll!': ")
print(v.lower().replace("kurat","*****"))



#korralik nimi
nimi = input("Siia nimi: ")
puh_nimi = nimi.strip().capitalize()
print("Tere,", puh_nimi+"!")