digits = input()

d = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

ans = [""]

for num in digits:
    temp = []

    for x in ans:
        for ch in d[num]:
            temp.append(x + ch)

    ans = temp

print(ans)