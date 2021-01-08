# Variables
num1 = 3
num1t = 3
num2 = 5
num2t = 5
num3 = 15
num3t = 15
total = 0


# Main Loops
while num1t < 1000:
    total += num1t
    num1t += num1


while num2t < 1000:
    total += num2t
    num2t += num2

while num3t < 1000:
    total -= num3t
    num3t += num3


# Display
print(total)