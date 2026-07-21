#Percentage and Average Calculator
sub1=int(input("Enter marks of subject1:"))
sub2=int(input("Enter marks of subject2:"))
sub3=int(input("Enter marks of subject3:"))
sub4=int(input("Enter marks of subject4:"))
sub5=int(input("Enter marks of subject5:"))
total_marks=sub1+sub2+sub3+sub4+sub5
print("Total_marks:",total_marks)
Avg=total_marks/5
print('Average:',Avg)
percentage = (total_marks / 500) * 100
print("Percentage:", percentage, "%")
