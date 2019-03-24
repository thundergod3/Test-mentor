NumerList = [10,-22,200,124125,12]

for i in NumerList:
    print(i)

Input = input('Ban muon xoa so dau hay cuoi')

if(Input == 'dau'):
    NumerList.pop(0)
    for j in NumerList:
        print(j)

if(Input == 'cuoi'):
    NumerList.pop(len(NumerList)-1)
    for k in NumerList:
        print(k)