Ora = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
Temperatura = [0,-1,-2,-3,-4,-5,-4,-3,-2,-2,-1,0,0,1,2,3,4,5,6,5,4,3,2,1]
print('a.) Temperatura medie:',round((sum(Temperatura)/24),1))
print('b.) Maximul temperaturii:',max(Temperatura))
print('    Minimul temperaturii:',min(Temperatura))
x1=Ora[Temperatura.index(max(Temperatura))]
if (Temperatura.count(max(Temperatura))) > 1 :
    del(Temperatura[Temperatura.index(max(Temperatura))])
    print(Temperatura)
    x2=Ora[Temperatura.index(max(Temperatura))]
    print('c.) Temperatura maxima s-a inregistrat la orele:',x1,',',(x2+1))
else :
    print('c.) Temperatura maxima s-a inregistrat la orele:',x1)

y1=Ora[Temperatura.index(min(Temperatura))]
if (Temperatura.count(min(Temperatura))) > 1 :
    del(Temperatura[Temperatura.index(min(Temperatura))])
    print(Temperatura)
    y2=Ora[Temperatura.index(min(Temperatura))]
    print('d.) Temperatura minima s-a inregistrat la orele:',y1,',',(y2+1))
else :
    print('d.) Temperatura minima s-a inregistrat la orele:',y1)