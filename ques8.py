N = int(input("Enter N: "))
count = 0
while N > 0:
    count += 1
    N //= 10
print("Digit count =",count)