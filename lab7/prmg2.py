def temperature_converter():
    print("temperature converter")
    temp =float(input("enter temperature:"))
    print("convert to:")
    print("1. celsius to fahrenheit")
    print("2. Fahrenheit to clsius")
    choice = input("enter choice(1/2):")
    if choice =="1":
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}C is {fahrenheit}F")
    elif choice == '2':
        celsius = (temp - 32) * 5/9
        print(f"{temp}F is {celsius}C")
     
    else:
        print("invalid input")
temperature_converter()        
