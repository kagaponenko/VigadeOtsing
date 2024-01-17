# print("Tere maailm!")
# nimi=input("Mis on sinu nimi?")
# vanus=int(input("Kui vana sa oled?")) #kommentaar

# print("Tere "+nimi+"! Sa oled "+str(vanus)+" aastat vana.")
# print("Tere",nimi,"! Sa oled",vanus,"aastat vana.")
# print("Tere {0}! Sa oled {1} aastat vana.".format(nimi,vanus))

# print(type(nimi))
# print(type(vanus))

# arv1=float(input("Arv 1: "))
# t=input("Tehe: ")
# arv2=float(input("Arv 2: "))
# vastus=eval(str(arv1)+t+str(arv2))
# print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus))


##2
# vanus=18
# eesnimi="Jaak"
# pikkus=16.5
# kas_kaib_koolis=True

# print("Muutuja",vanus,"on",type(vanus))
# print("Muutuja",eesnimi,"on",type(eesnimi))
# print("Muutuja",pikkus,"on",type(pikkus))
# print("Muutuja",kas_kaib_koolis,"on",type(kas_kaib_koolis))


##3
#from random import * #koik funktsioonid mis on moodulis
#kogus=randint(1,100)
#print("Kokku on",kogus,"kommid")
#mitu=int(input("Mitu kommi tahad votta?"))
#kogus=kogus-mitu
#print("Laua peal on",kogus,"kommid")


##4
# from math import *
# l=float(input("Umbermoot: "))
# d=round(l/pi,2) #3.14...
# print("Labimoot=",d)


##5
# from math import *
# N=float(input("N: "))
# M=float(input("M: "))
# diag=sqrt(M**2+N**2)
# print("diag=",round(diag,2))


##6
# aeg = float(input("Mitu tundi kulus soiduks? "))
# teepikkus = float(input("Mitu kilomeetrit soitsid? "))
# kiirus = aeg / teepikkus

# print("Sinu kiirus oli " + str(kiirus) + " km/h")


##7
# arv1=int(input("arv1: "))
# arv2=int(input("arv2: "))
# arv3=int(input("arv3: "))
# arv4=int(input("arv4: "))
# arv5=int(input("arv5: "))
# keskmine=(arv1+arv2+arv3+arv4+arv5)/5
# print("avg=",round(avg,2))


from random import randint

a1=randint(1,50)
a2=randint(1,50)
a3=randint(1,50)
a4=randint(1,50)
a5=randint(1,50)
keskmine=(a1+a2+a3+a4+a5)/5
print("Arvud=",round(avg,2)) #


##8
# print("   @..@")
# print("  (----)")
# print(" ( \__/ )")
# print(" ^^ \"\" ^^")


# print("@..@".center(10))
# print("(----)".center(10))
# print("( \__/ )".center(10))
# print("^^ \"\" ^^".center(10))


##9
# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# P=a+b+c
# print("P=",round(P,2))


##10
# pitsa=12.90
# hind=12.90/2+12.90*0.1/2
# print("hind=",round(hind,2))