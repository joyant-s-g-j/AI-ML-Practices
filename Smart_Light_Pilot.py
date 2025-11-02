numbers = input().split()

brightness = float(numbers[0])
threshold = float(numbers[1])

if brightness >= threshold:
    print("ON")
else:
    print("OFF")