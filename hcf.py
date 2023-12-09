a = int(input("enter first number: "))
b = int(input("enter second number: "))
if a>b:
    min = b
else:
    min = a

for i in range (1, min+1):
    if ((a % i == 0) and (b % i == 0)):
        hcf = i

print(f"the hcf of a and b is : {hcf}")


