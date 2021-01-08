# Variables
total = 1


# Functions
def GCD(a:int,b:int):
    if b == 0 or a == 1:
        return(a)
    return(GCD(b,a%b))


# Main Loop
for i in range(1,21):
    divider = GCD(total, i)
    total *= i
    total /= divider


# Display
print(total)