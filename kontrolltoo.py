        #1
n=int(input("Любое число от 1 до 9: "))
for i in range(0, n):
    print(" ^---^  ",end=" ")
print()
for i in range(0, n):
    print("( o o ) ",end=" ")
print()
for i in range(0, n):
    print(" ! = !/)",end=" ")
print()
print()


        #2
n=int(input("Введите число n: "))
a=int(input("Введите степень: "))
B=1
while True:
    C=B**a
    if C>n*100:
        break
    print(C)
    B+=1
print()
    

        #3
from random import randint
m=0
U=randint(1,30)
print("В классе",U, "человек(а)")
maxO=0
minO=5
while (m<U):
    O=randint(1,5)
    maxO=max(maxO,O)
    minO=min(minO,O)
    m+=1
    print("Оценка",m,"ученика", O)
    if m==U:
        break
print("Минимальная оценка", minO)
print("Максимальная оценка", maxO)
print()


        #4
A=1
T=0
while True:
    T+=3
    A*=2
    print("Прошло",T,"часов","стало", A,"амеб")
    if T==24:
        break
print()


        #5
from random import randint
K=randint(1,100)
M=randint(1,10)
s=0
t=0
print("у губки боба всего",K, "котлет(ы)")
print("на одну сковородку помещается",M, "котлет(ы)")
while (K>0):
    K-=1
    s+=1
    if(s==M):
        t+=1
        s=0
print("надо пожарить",t, "полных сковородок")
print("на последней сковородке останется дожарить",s, "котлет(ы)")