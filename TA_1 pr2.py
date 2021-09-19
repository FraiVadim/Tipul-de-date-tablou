Zi = ['L', 'Ma', 'Mi', 'J', 'Vi', 'S', 'D']
Venit = [145,167,584,283,829,192,182] 
print('a.) Venitul saptamanal:', sum(Venit))
print('b.) Media venitului zilnic:', sum(Venit)/7)
print('c.) Ziua cu cel mai mare venit:',Zi[Venit.index(max(Venit))])
print('d.) Ziua cu cel mai maic venit:',Zi[Venit.index(min(Venit))])