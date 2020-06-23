print("Welcome to the Python Calculator!")

name = input("To start the calculator first enter your name below: \n").lower().title()

n1 = int(input(f"Hey {name}, Enter your first number to enter in the calculator as number 1 below: \n"))

n2 = int(input("Enter your second number to enter in the calculator as number 2 below: \n"))

addition = n1 + n2
subtraction = n1 - n2
product = n1 * n2
division = n1 / n2
remainder = n1 % n2
exponent = n1 ** n2

print(f'''
Addition:
------------------------------------------------------------------
{n1} + {n2} is: {addition}
------------------------------------------------------------------
Subtraction:
------------------------------------------------------------------
{n1} - {n2} is: {subtraction}
------------------------------------------------------------------
Multiplication:
------------------------------------------------------------------
{n1} x {n2} is: {product}
------------------------------------------------------------------
Division:
------------------------------------------------------------------
{n1} ÷ {n2} is: {division} and the remainder is: {remainder}
------------------------------------------------------------------
Sorry, I don't want to put the exponent because the answer can be very very big... If you want to add it read the README.md file.
------------------------------------------------------------------
Thank you for using qwerty14IRahman1's Python Calculator {name}!!''')