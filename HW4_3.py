def climb(n):
    if n<3:
        return n
    return climb(n-1)+climb(n-2)

n = int(input())
z = climb(n)
print(z)