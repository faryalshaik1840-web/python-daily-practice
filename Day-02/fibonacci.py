# Program to print Fibonacci series

terms = int(input("Enter the number of terms: "))

first = 0
second = 1

print("Fibonacci Series:")

for i in range(terms):
    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number
