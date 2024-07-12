def alg(a,b):
    if a==0 or b==0:
        return a+b
    if a>b:
        a = a%b
        return alg(a,b)
    else:
        b= b%a
        return alg(a,b)

a = int(input())
b = int(input())
z = alg(a, b)
print(z)