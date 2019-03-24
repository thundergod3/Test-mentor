#Tìm số bé nhất của dãy số

NumerList = [10,-22,200,124125,12]
print(min(NumerList))

#Tìm giai thừa
Input = int(input('Nhập số cần tính giai thừa'))

def giaithua(n):
    if(n == 1):
        return 1
    else: 
        return n * (giaithua(n-1))


print('Giai thừa của', Input, 'là', giaithua(Input))

#Tìm ước chung lớn nhất
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a % b)

print(gcd(100,2000))

#Tính 1 số trong dãy fibbonacii 
def f(n):
    if n == 0: return 1
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input("Nhập số n: "))
print (f(n))

#Đảo ngược 1 dãy số
for i in reversed(NumerList):
    print(i)

#Đảo ngược 1 dãy string

s = 'hello world'
s = s[::-1]
print(s)