#alphabet_pyramid.py
n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    ch=65
    for k in range(1,i+1):
        print(chr(ch),end="")
        ch+=1
    ch-=2
    for l in range(i-1,0,-1):
        print(chr(ch),end="")
        ch-=1
    print()
