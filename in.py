# while True:
#     try:
#         pikkus=int(input("Pikkus: "))
#         laius=int(input("Laius: "))
#         if pikkus>0 and laius>0:
#             print("Pindala: ",pikkus*laius)
#             print("Pikkus ja laius on sissetanud ja pindala on leidnud")
#         else:
#             print("on vaja andmeid suurem kui 0")
#         break
#     except:
#         print("On vaja int formaat kasutada!")
# print("Too lopp")

            # print("Tere! Olen sinu uus sõber - Python!")
            # nimi=input("Mis on sinu nimi?")
            # print(nimi,", oi kui ilus nimi!")
            # v=int(input(nimi,"! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
            # # input()->"0" or "1", int(input())- 0 or 1
            # if v==1: #if v=="1"
            #     print("Indexi leidmine")
            #     while True:
            #         try:
            #             pikkus=int(input("Pikkus: "))
            #             mass=float(input("Kaal: "))
            #             break
            #     except:
            #         print("Viga!")
            #     index=mass/(0.01pikkus)2                              ##
            #     if index<16:
            #         print(Tervisele ohtlik alakaal)
            #     elif index<19:
            #         print(Alakaal)
            #     elif index<25:
            #         print(Normaalkaal)
            #     elif index<30:
            #         print(Ülekaal)
            #     elif index<30:
            #         
            # else:
            #     print("Kahju! See on vaga kasulik info!")
    



# while True:
#     vastus=input("Tahan komme!")
#     if vastus.lower()=="komm":
#         break
#     else:
#         print("Koik raagivad "+vastus)
        

# vastus=""
# while vastus.lower()!="komm":
#     vastus=input("Tahan komme!")
    

# for in range(10,-2,1): #1.i=0,2.i=1,...,10.i=9
#     print(i,"samm")

# for in range(15): #1-14, samm=1
#     print(i)

# for in range(10):
#     n=input("Nimi: ")
#     print("Tere",n)

# for in range(10,0,-2):
#     print(i)
    



    #1
# print("1. vaariant")
# mitu=0
# for k in range(1,16):
#     n=float(input("Sisesta"+str(k)+". arv"))
#     if int(n)==float(n):
#         mitu+=1
# print("Taisarvude kogus: ",mitu)


# print("2. vaariant")
# k=0
# mitu=0
# while True:
#     k+=1
#     n=float(input("Sisesta"+str(k)+". arv"))
#     if int(n)==float(n):
#         mitu+=1
#     if k==15: break


# print("3. vaariant")
# k=0
# mitu=0
# while k<15:
#     k+=1
#     n=float(input("Sisesta"+str(k)+". arv"))
#     if int(n)==float(n):
#         mitu+=1
        



    #3
# print("vaariant for")
# from random import *
# p=1
# for i in range(8):
#     a=randint(-10,10)
#     print(a)
#     if a>0: p*=a
# print("произведение чисел =",p)

# print("vaariant while")
# from random import *
# p=1
# k=0
# while k<8:
#     k+=1
#     a=randint(-10,10)
#     print(a)
#     if a>0: p*=a
# print("произведение чисел =",p)

# print("vaariant while True")
# from random import *
# p=1
# k=0
# while True:
#     if (k==8):
#         break
#     k+=1
#     a=randint(-10,10)
#     print(a)
#     if a>0: p*=a
# print("произведение чисел =",p)    




    #31 for, while(True)
# print("vaariant for")
# from random import *
# K=randint(1,100)
# M=randint(1,10)
# s=0
# p=0
# print("у губки боба всего",K, "котлет(ы)")
# print("на одну сковородку помещается",M, "котлет(ы)")
# for b in range(0,K):
#     s+=1
#     if(s==M):
#         p+=1
#         s=0
# print("надо пожарить",p, "полных сковородок")
# print("на последней сковородке останится дожарить",p, "котлет(ы)")

# print("vaariant while")
# from random import *
# K=randint(1,100)
# M=randint(1,10)
# s=0
# p=0
# print("у губки боба всего",K, "котлет(ы)")
# print("на одну сковородку помещается",M, "котлет(ы)")
# while(K>0):
#     K-=1
#     s+=1
#     if(s==M):
#         p+=1
#         s=0
# print("надо пожарить",p, "полных сковородок")
# print("на последней сковородке останится дожарить",p, "котлет(ы)")

# print("vaariant while True")
# from random import *
# K=randint(1,100)
# M=randint(1,10)
# s=0
# p=0
# print("у губки боба всего",K, "котлет(ы)")
# print("на одну сковородку помещается",M, "котлет(ы)")
# while True:
#     K-=1
#     s+=1
#     if(s==M):
#         p+=1
#         s=0
#     if(K==0):
#         break
# print("надо пожарить",p, "полных сковородок")
# print("на последней сковородке останится дожарить",p, "котлет(ы)")




        #+(7)




            ##24.01
# from datetime import *
# from random import *
# arve_nr= date.today()#datetime.now()
# tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
# summa=0

# tooded=["Piim","Leib","Kommid","Voi"] #len(tooded)=3
# for i in range(len(tooded)): #tooded[0]="Piim", tooded[1]="Leib", tooded[2]="Kommid"
#     toode=tooded[i]
#     hind=randint(50,150)/100
#     v=input("Toode:"+toode+"Hind:"+str(hind)+"\nKas tahad osta?").lower()
#     if v=="jah":
#         mitu=int(input("Mitu?"))
#         tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
#         summa=+mitu*hind
        
# tsekk+="Kokku maksta: "+str(summa)
# print(tsekk)




#praktiline too
#Ulesanne 1
# from datetime import *
# from random import *
# nimi=input("Palun sisesta oma nimi:")
# mitu=int(input("Mitu korda tervitada? "))
# for i in range(mitu):
#     print(f"Ole tervitatu, {nimi}, {i+1}. korda.")

#Ulesanne 1
# from datetime import *
# from random import *
# sum_=0
# for i in range(10):
#     arv=int(input("Sisesta arv: "))
#     sum_+=arv
# print(f"Summa= {sum_}")




# print("*** ИГРЫ С ЧИСЛАМИ ***")
# print()
# #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# while 1: #1=True
#     try:
#         a=abs(int(input("Введите целое число => ")))
#         break
#     except ValueError:
#         print("Это не целое число")
# #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# if a==0: #== -равно ли 0
#     print("Нет смысла ничего делать с нулём")
# else:
# #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#     print("Определяем, сколько в числе чётных и сколько нечётных цифр")
#     print()
#     c=b=a
#     paaris=0
#     paaritu=0
#     while b>0:
#         if b%2==0:
#             paaris+=1
#         else:
#             paaritu+=1
#             b=b//10
    
#     print("Чётных цифр:"+str(paaris))
#     print("Нечётных цифр:"+str(paaritu))
#     print()
# #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#     print("*Переворачиваем* введённое число")
#     print()
#     b=0
#     while a>0:
#         number=a%10
#         a=a//10
#         b=b*10
#         b+=number
#     print("*Перевёрнутое* число", b)
#     print()
# #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#     print("Проверяем гипотезу Сиракуз")
#     print()
#     if c%2==0:
#         print(f"{c} - чётное число. Делим на 2.")
#     else:
#         print(f"{c} - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
#     while c!=1:
#         if c%2==0:
#             c=c/2
#         else:
#             c=(3*c+1)/2
#         print(c,end="\t")
#     print()
#     print("Гипотеза верна")




        #1
# from datetime import *
# from random import *
# m=0
# n=int(input("Любое число от 1 до 9: "))
# while True:
#     if 1<=n<=9:
#         print("^---^".center(8))
#         print("( o o )".center(8))
#         print(" ! = !/)".center(8))
#         m+=1
#     if 1>n>9:
#         break
#     if m==n:
#         break
    
        #2
# from random import *
# from random import randint
# m=0
# U=randint(1,5) #30
# print ("В классе",U, "человек(а)")
# G=[random.randit(1,5) for _ in range(U)]
# m+=1
#     if m==U:
#     break

# arv1=int(input("arv1: "))
# # arv2=int(input("arv2: "))
# # arv3=int(input("arv3: "))
# # arv4=int(input("arv4: "))
# # arv5=int(input("arv5: "))
# # keskmine=(arv1+arv2+arv3+arv4+arv5)/5
# # print("avg=",round(avg,2))


# from random import randint

# a1=randint(1,50)
# a2=randint(1,50)
# a3=randint(1,50)
# a4=randint(1,50)
# a5=randint(1,50)
# keskmine=(a1+a2+a3+a4+a5)/5

# # O=randint(1,5)


    #31 for, while(True)
print("vaariant for")
from random import *
K=randint(1,100)
M=randint(1,10)
s=0
p=0
print("у губки боба всего",K, "котлет(ы)")
print("на одну сковородку помещается",M, "котлет(ы)")
for b in range(0,K):
    s+=1
    if(s==M):
        p+=1
        s=0
print("надо пожарить",p, "полных сковородок")
print("на последней сковородке останится дожарить",p, "котлет(ы)")

# print("vaariant while")
# from random import *
# K=randint(1,100)
# M=randint(1,10)
# s=0
# p=0
# print("у губки боба всего",K, "котлет(ы)")
# print("на одну сковородку помещается",M, "котлет(ы)")
# while(K>0):
#     K-=1
#     s+=1
#     if(s==M):
#         p+=1
#         s=0
# print("надо пожарить",p, "полных сковородок")
# print("на последней сковородке останится дожарить",p, "котлет(ы)")

# print("vaariant while True")
# from random import *
# K=randint(1,100)
# M=randint(1,10)
# s=0
# p=0
# print("у губки боба всего",K, "котлет(ы)")
# print("на одну сковородку помещается",M, "котлет(ы)")
# while True:
#     K-=1
#     s+=1
#     if(s==M):
#         p+=1
#         s=0
#     if(K==0):
#         break
# print("надо пожарить",p, "полных сковородок")
# print("на последней сковородке останится дожарить",p, "котлет(ы)")