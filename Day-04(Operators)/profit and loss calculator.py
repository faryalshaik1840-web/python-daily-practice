#Profit and Loss Calculator
cp=int(input("Enter costprice:"))
sp=int(input("Enter sellingprice:"))
if sp>cp:
    print("profit")
elif sp<cp:
    print("Loss")
else:
    print("No Profit No Loss")
    
    
