#GST CALCULATOR
productprice=int(input("Enter a product:"))
Gst=int(input("Enter GST:"))
GstAmount=(productprice*Gst)/100
print(GstAmount)
print(productprice+GstAmount)
