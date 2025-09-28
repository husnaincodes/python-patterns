
rows =  int(input("Enter the number of Pattern: "))
for i in range(rows):
    if  i == 0 or i == rows-1:
        print("*"*rows)
    else:
        print("*"+" "*(rows-2)+"*")
