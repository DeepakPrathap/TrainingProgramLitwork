
n = list(map(int, input().split()))
a, b = n[0], n[1] if len(n) > 1 else 1

s = str(a)
odd, even = "+", "/"

for x in range(a - 1, b - 1, -1):
    if (x + 1) % 2:
        s += odd + str(x)
        odd = "-" if odd == "+" else "+"
    else:
        s += even + str(x)
        even = "*" if even == "/" else "/"

print(eval(s.replace("/", "//")))

