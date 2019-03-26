number_list = [10,-22,200,124125,12]

for i in number_list:
    print(i)

Input = input('Ban muon xoa so dau hay cuoi')

if(Input == 'dau'):
    number_list.pop(0)
    for j in number_list:
        print(j)

if(Input == 'cuoi'):
    number_list.pop(len(number_list)-1)
    for k in number_list:
        print(k)