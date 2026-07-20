cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))
if sp > cp:
    print("Profit")
elif sp < cp:
    print("Loss")
else:
    print("No Profit No Loss")
