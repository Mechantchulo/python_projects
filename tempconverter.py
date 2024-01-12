'''Write a convertToFahrenheit() function with a degree celcius parameter
This function returns the number of this temperature in degrees fahrenheit.Then write a function named
ConvertToCelsius() with a degree fahrenheit parameter and it returns a number of this temperature in degree celcius  '''

'''use the formula below
Farenheit = celcius * (9/5) + 32
Celsius = (Farenheit - 32) * (5/9)''' 


print("Temperature conversion program")
print("celsius_to_fahrenheit")
print("fahrenheit_to_celsius")

choice = input("Enter choice (1 or 2):")

if choice == "1":
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} degrees celsius is equal to {fahrenheit} degrees Fahrenheit")

elif choice == "2":
    fahrenheit = float(input("Enter the temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius")#print(f"{}") is string fromatting

else:
    print("Invalid choice.Please choose 1 or 2")
 