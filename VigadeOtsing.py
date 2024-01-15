from math import *  #неправильная расстановка слов
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #float
S=a**2
print("Ruudu pindala", round(S,1)) #(округление)
P=4*a
print("Ruudu umbermoot", round(P,1)) #неправильные кавычки, (округление)
di=a*sqrt(2) #неправильная запись функции
print("Ruudu diagonaal", round(di,2))
print()
print("Ristkuliku karakteristikud") #лишняя закрывающая скобка
b=float(input("Sisesta ristkuliku 1. kulje pikkus => ")) #float
c=float(input("Sisesta ristkuliku 2. kulje pikkus => ")) #float
S=b*c
print("Ristkuliku pindala", round(S,1)) #не было открывающих кавычек, (округление)
P=2*(b+c) #не было знака умножения
print("Ristkuliku umbermoot", round(P,1)) #(округление)
di=sqrt(b**2+c**2) #неправильная запись функции, не было 2го знака умножения х2
print("Ristkuliku diagonaal", round(di,1)) #не было закрывающей скобки, (округление)
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #неправильно стоят квычки, лишняя закрывающая скобка, float
d=2*r #не было знака умножения
print("Ringi labimoot", d) #не было запятой
S=pi*r**2 #не было 2го знака умножения, лишние скобки
print("Ringi pindala", round(S,2)) #(округление)
C=2*pi*r #не было знака умножения, лишние скобки
print("Ringjoone pikkus", round(C,2)) #не было закрывающей скобки, (округление)