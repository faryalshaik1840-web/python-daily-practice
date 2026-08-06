#hollow_sandglass_pattern.py
n=int(input("Enter a number:"))
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(2,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
