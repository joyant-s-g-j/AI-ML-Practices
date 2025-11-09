st = input().lower()
d = {}
for i in st:
    if i.isalpha():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

for key, value in sorted(d.items()):
    print(f"{key} : {value}")