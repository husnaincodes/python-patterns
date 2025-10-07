
rows = int(input("Enter the number : "))

for i in range(1 ,rows+1):

    print(" "*(rows-i),end="")

    for j in range (1,1+i):

        print(j,end=" ")
    print()