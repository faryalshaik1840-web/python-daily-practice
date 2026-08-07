#hollow_pyramid_pattern
n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if i==n or k==0 or k==2*i-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
