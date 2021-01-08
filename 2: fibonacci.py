# Variables
incheck = True
i = 1
total = 0


# Functions
def fib(n: int):
    sums = 0
    num1 = 4
    num2 = 6
    if n == 1:
        return 4
    elif n == 2:
        return 6
    else:
        for i in range(n-2):
            i = i
            sums = num2 + num1
            num1 = num2 
            num2 = sums
    return sums


# Main Loop
while incheck == True:
    num = fib(i)
    i += 1
    if num%2 == 0:
        total += num
    if num > 4000000:
        incheck = False


# Display
print(total)