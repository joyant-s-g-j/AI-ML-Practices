n = int(input())

for i in range(n):
    num = input()
    if "010" in num or "101" in num:
        print("Good")
    else:
        print("Bad")