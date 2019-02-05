n = 0
for a in range(100, 999):
    for b in range(100, a):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b
print(n)