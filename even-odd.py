"""Write  two functions isOdd() and isEven()with a single numeric parameter named number.
The isOdd function returns TRUE if number is odd and vice-versa"""

#create a variable called number where it stores the value of the number.

number = int(input("Enter the number: "))

#defining the first function

def number_isOdd():
    return number % 2

#defining the second function
def number_isEven():
    return number % 2

#The conditional texts
if number % 2 == 0:
    print(True)

else:
    print(False)             
