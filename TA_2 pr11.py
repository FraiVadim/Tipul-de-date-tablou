import copy
n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
if n<10:
    for i in range(0,n):
        x=int(input('Dati elementul='))
        a.extend([x])
print(a)

print('a) Componentele tabloului la un interval de 5 poziţii:',a[::5])

print('b) Numerele în ordinea inversă a introducerii în calculator:',a[::-1])

b=sorted(a)
b.sort(reverse=True)
print('c) Componentele tabloului în ordine descrescătoare:',b)

c=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        c.extend([y])
print('d) Componentele pare:',c)

print('e) Media aritmetică a componentelor pare:',sum(c))

f=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        y=a[i]
        f.extend([y])
print('f) Afişează pe ecran doar componentele impare:',f)

g=[]
x=int(input('dati x: '))
y=int(input('dati y: '))
for i in range(0,len(a)):
    if a[i]>x and a[i]%y!=0:
        z=a[i]
        g.extend([z])
if len(g)>0:
    print('g) Componentele care sunt mai mari ca x şi nu sunt divizibile cu y:',g)
else:
    print('g) Nu sunt asa componente.')

h=[]
x=int(input('dati x: '))
y=int(input('dati y: '))
for i in range(0,len(a)):
    if a[i]>x and a[i]<y:
        z=a[i]
        h.extend([z])
if len(h)>0:
    print('h)  Componentele care sunt mai mari ca x şi mai mici decât y:',h)
else:
    print('h) Nu sunt asa componente.')

j=[]
for i in range(0,len(a)):
    if a[i]%2!=0 and a[i]<0:
        z=i
        j.extend([z])
if len(j)>0:
    print('i) Poziţiile (indicii) componentelor impare negative. In informatica numerotarea incepe de la 0:',j)
else:
    print('i) Nu sunt componente impare negative.')

j=[]
for i in range(0,len(a)):
    if a[i]>9 and a[i]<100:
        z=i
        j.extend([z])
if len(j)>0:
    print('j) Poziţiile (indicii) componentelor ce conţin doar două cifre semnificative:',j,)
else:
    print('j) Nu sunt componente ce contin doar doua cifre semnificative.')

k=copy.copy(a)
k.pop(0)
k.insert(0,min(a))
print('k) Inlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv:',k)

l=copy.copy(a)
l.pop(l.index(min(l)))
l.insert(a.index(min(a)),a[0])
print('l) Inlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia:',l)

n=int(input('Dati numarul de elemente din noul tablou:'))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul='))
    a.extend([x])
m=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        m.extend([y])
print('m) Un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură:',m)

n=int(input('Dati numarul de elemente din noul tablou:'))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul='))
    a.extend([x])
n=[]
for i in range(0,len(a)):
    if a[i]%3==0:
        y=a[i]
        n.extend([y])
print('n) Un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură:',n)

n=int(input('Dati numarul de elemente din noul tablou:'))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul='))
    a.extend([x])
o=[]
s=0
numere_prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
for i in range(0,len(a)):
    for j in range(0,len(numere_prime)):
        if a[i]%numere_prime[j]==0:
            s=s+1
    if s<5:
        z=a[i]
        o.extend([z])
    s=0
print('o) Un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori:',o)