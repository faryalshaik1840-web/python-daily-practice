#compount Interest
p=int(input("Enter principal:"))
r=int(input("Enter Rate:"))
t=int(input("Enter Time:"))
A=p*(1+r/100)**t#20
ci=A-p
print(A)
print(ci)
