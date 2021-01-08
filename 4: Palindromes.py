# Variables
biggest = 0


# Functions
def pcheck(n):
    templist = []
    for i in range(len(str(n))):
        templist.append(str(n)[i])
    for i in range(int(len(templist)/2)):
        x = i + 1
        if templist[i] != templist[-x]:
            return False
    return True


# Main Loop
for i in range(100, 1000):
    for x in range(100,1000):
        num = i*x
        true = pcheck(num)
        if true == True:
            print(str(i) + " " + str(x) + " " + str(num))
            if num > biggest:
                biggest = num
print(biggest)

