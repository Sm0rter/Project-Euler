# Variables
stotal = 0
ctotal = 0



# Calculating
for i in range(1, 101):
    stotal += i ** 2

for i in range(1,101):
    ctotal += i ** 3

difference = ctotal - stotal


# Display
print(difference)