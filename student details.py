#prompting the user to input their details.
First_name = input("What is your name: ")
Second_name = input("What is your second name: ")
Faculty_name = input("What faculty are you in: ")
Year_of_study = float(input("Type in the year of study: "))
course_name = input("What course are you studying: ")
Student_number = input("Registration number: ")
Age = float(input("Type in your age: "))

#displaying the student details
print(f"Hello { First_name } { Second_name } REG.NO { Student_number }.Welcome to the  { Faculty_name } and congratulations for choosing { course_name }.")
