#prime_numbers_in_range
start=int(input("Enter starting number:"))
end=int(input("Enter ending number:"))
while(start<=end):
    if(start>1):
        i=1
        count=0
        while(i<=start):
            if(start%i==0):
                count+=1
            i+=1
        if(count==2):
            print(start)
    start+=1
