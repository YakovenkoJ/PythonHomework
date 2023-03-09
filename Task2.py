n = int(input("Input 3-digits number: "))
m = n // 100
k = n % 100 // 10
s = n % 10
print(f"Result: {m + k + s}")