
rows = 5
#upper part
for i in range (1 , rows+1):
    print("*"*i +" "*(2*(rows-i) )+"*"*i)

#lower part
for i in range (rows ,0 ,-1):
    print("*"*i +" "*(2*(rows-i) )+"*"*i)