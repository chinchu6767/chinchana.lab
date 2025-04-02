
def temperature_converter():
    print("Temperature Converter")
    temp = float(input("Enter temperature: "))
    print("Convert from:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    from_choice = input("Enter choice (1/2/3): ")
    
    print("Convert to:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    to_choice = input("Enter choice (1/2/3): ")
    
    if from_choice == "1":  
        if to_choice == "2":
            result = (temp * 9/5) + 32 
            print(f"{temp}C is {result}F")
        elif to_choice == "3":
            result = temp + 273.15
            print(f"{temp}C is {result}K")
        else:
            print("Invalid conversion choice.")
    
    elif from_choice == "2":  
        if to_choice == "1":
            result = (temp - 32) * 5/9  
            print(f"{temp}F is {result}C")
        elif to_choice == "3":
            result = (temp - 32) * 5/9 + 273.15  
            print(f"{temp}F is {result}K")
        else:
            print("Invalid conversion choice.")
    
    elif from_choice == "3":  
        if to_choice == "1":
            result = temp - 273.15  
            print(f"{temp}K is {result}C")
        elif to_choice == "2":
            result = (temp - 273.15) * 9/5 + 32 
            print(f"{temp}K is {result}F")
        else:
            print("Invalid conversion choice.")
    else:
        print("Invalid input.")

temperature_converter()
