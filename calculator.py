#simple python calculator program
#addition
def add(x, y):
    return(x + y)

#subtraction
def subtract(x,y):
    return(x-y)

#division
def divide(x,y):
    if y == 0:
        return("cannot divide by zero!")
    return(x/y)


#multiplication
def multiply(x,y):
    return(x * y)


print("welcome to the calculator")


#while true is an infinite loop
while True:
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice = input("enter your choice(1-5): ")

    if choice=='5':
        print("goodbye")
        break
    

    num1=float(input("enter first number"))
    num2=float(input("enter second number"))

    if choice == '1':
        result=add(num1,num2)
    elif choice=='2':
        result=subtract(num2,num2)
    elif choice=='3':
        result=multiply(num1,num2)
    elif choice=='4':
        result=divide(num1,num2)
    else:
        print("invalid input")
        continue
    print("Result:",result)


