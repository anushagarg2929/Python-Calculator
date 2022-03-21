firstNumber = input("enter first number : ")
operator = input("enter a operator (+,-,*,/,%) : ")
secondNumber = input("enter second number : ")

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

if operator == "+":
    print(firstNumber+secondNumber);
elif operator == "-":
    print(firstNumber - secondNumber);
elif operator == "*":
    print(firstNumber * secondNumber);
elif operator == "/":
    print(firstNumber / secondNumber);
elif operator == "%":
    print(firstNumber % secondNumber);
else :
    print("Invalid Operation")