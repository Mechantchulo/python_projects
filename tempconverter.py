'''Write a convertToFahrenheit() function with a degree celcius parameter
This function returns the number of this temperature in degrees fahrenheit.Then write a function named
ConvertToCelsius() with a degree fahrenheit parameter and it returns a number of this temperature in degree celcius  '''

'''use the formula below
Farenheit = celcius * (9/5) + 32
Celsius = (Farenheit - 32) * (5/9)''' 

#Display the options to choose btn the two
print("Temperature conversion program")
print("celsius_to_fahrenheit")
print("fahrenheit_to_celsius")

#Getting the user to choose which option they want to use to convert their temp
choice = input("Enter choice (1 or 2):")

if choice == "1":
    celsius = float(input("Enter temperature in celsius: "))#program prompt user to input the temp value in celsius
    fahrenheit = (celsius * 9/5) + 32#Conversion occurs here
    print(f"{celsius} degrees celsius is equal to {fahrenheit} degrees Fahrenheit")#dsiplaying the results

elif choice == "2":
    fahrenheit = float(input("Enter the temperature in fahrenheit: "))#program prompt user to input the temp value in fahrenheit
    celsius = (fahrenheit - 32) * 5/9#Conversion occurs here
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius")#print(f"{}") is string fromatting

else:
    print("Invalid choice.Please choose 1 or 2")#if choice is not within the two conversion options.
 
