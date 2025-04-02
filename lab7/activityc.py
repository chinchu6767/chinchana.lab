def find_largest():
    print("Find the largest of five numbers")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    num4 = float(input("Enter fourth number: "))
    num5 = float(input("Enter fifth number: "))

    largest = max(num1, num2, num3, num4, num5)

    print(f"The largest number is: {largest}")

find_largest()
