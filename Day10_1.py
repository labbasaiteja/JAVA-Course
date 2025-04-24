n,p = input().split()
n = int(n)
p = int(p)
res = 1

for i in range(p):
    res *= n

print(res)    