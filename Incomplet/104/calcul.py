h = 1
N = 2**h - 1

while N < 10**4 :
    h += 1
    N = 2**h - 1

print(h)
