#reverse_repeated_alphabet_triangle.py
n=int(input("Enter a number:"))
for i in range(n,0,-1):
    ch=64+i
    for j in range(1,i+1):
        print(chr(ch),end="")
    print()
