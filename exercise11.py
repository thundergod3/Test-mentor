#Tìm số bé nhất của dãy số
number_list = [6, -4, 4, 8, -127, 5, 7, 2, 3, 9]

def find_lowest(lst):
    """Return the lowest positive number in a list."""
    def lowest(first, rest):
        # Base case
        if len(rest) == 0:
            return first
        if first > rest[0] or first < 0:
            return lowest(rest[0], rest[1:])
        else:
            return lowest(first, rest[1:])
    return lowest(lst[0], lst[1:])


print(find_lowest(number_list))

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
def reverse(q):
    if len(q) != 0:
        temp = q.pop(0)
        reverse(q)
        q.append(temp)
    return q

print(reverse(number_list))

#Đảo ngược 1 dãy string

def rreverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]

print(rreverse('hello world'))