n = int(input())
inp = list(map(int,input().split()))
for i in inp:
    m = max(inp)
inp.remove(m)
for j in inp:
    m1 = max(inp)
p = m * m1
print(p)
