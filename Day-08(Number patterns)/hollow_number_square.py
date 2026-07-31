#hollow_number_square.py
n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n:
            print(j,end="")
        elif j==1 or j==n:
            print(i,end="")
        else:
            print(" ",end="")
    print()
