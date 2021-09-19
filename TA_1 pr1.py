import copy
x=[1,2,3,4,5]
y=copy.copy(x)
print('a.)',x[1]+x[2]+x[3])
print('b.)', sum(y))
produs =1
for i in range (0 ,len(x)):
	produs=produs*x[i]
print('c.)',produs)
print('d.)',abs(x[2]))
print('e.)',x[0]+y[0])