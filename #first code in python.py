#first code in python 

print("Hello World")
print("Be welcome to our calculator")

numberA = int(input("Type your first number: "))
numberB = int(input("Type your second number: "))

operation = int(input("Type what kind of operation you wanna do: "
                      "\n1 - Addition "
                      "\n2 - Subtraction " 
                      "\n3 - Multiplication "
                      "\n4 - Division"
                      "--> "))

while operation <= 0  or operation >= 6:
    if operation == 1 : 
       result = numberA + numberB
    elif operation == 2 : 
       result = numberA - numberB
    elif operation == 3 : 
       result = numberA * numberB
    elif operation == 4 : 
       result = numberA / numberB
    else : 
        print("Error! Type a number between 1 and 4!")

print("Your result is: " + str(result))
