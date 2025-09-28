
rows = int(input("Enter the number of pattern: "))
for i in range(rows,0 , -1):

    print(" "*(rows - i)+"*"*(2*i-1))