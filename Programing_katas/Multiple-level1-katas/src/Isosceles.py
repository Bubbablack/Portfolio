
def isosceles(num):
    for i in range(1,num+1):
        for j in range (1,num-i+1):
            print(end=" ")
        for j in range (i,0,-1):
            print("#",end="")
        for j in range(2,i+1):
            print("#", end="")
        print()

isosceles(5)