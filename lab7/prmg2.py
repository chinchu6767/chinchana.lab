def factorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n*factorial(n-1)
    num = int(input("enter a number to find its factorial:"))
    print(f"the factorial of {num}is{factorial(num)}")