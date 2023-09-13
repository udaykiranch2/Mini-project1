import random
while True:
    #generating random numbers and performing random operation from given list
    num1 = random.randint(1,999)
    num2 = random.randint(1,999)
    operations = ['addition','subtraction','multiplication','division']
    operation = random.choice(operations)
    if num1 > num2:
        if operation == 'addition':
            sol = num1 + num2 
        elif operation == 'subtraction':
            sol = num1 - num2
        elif operation == 'multiplication':
            sol = num1 * num2 
        else:
            sol = num1 // num2 
    else:
        if operation == 'addition':
            sol = num1 + num2 
        elif operation == 'subtraction':
            sol = num2 - num1
        elif operation == 'multiplication':
            sol = num1 * num2 
        else:
            sol = num2 // num1

    #getting answer from user      
    if num1 > num2:
        get_sol = input(f"compute {operation} of {num1} and {num2}\n")
    else:
        get_sol = input(f"compute {operation} of {num2} and {num1}\n")

    if not get_sol:
        print("closing the quiz")
        break


    try:
        answer=float(get_sol)
        if answer== sol:
            print("correct")
        elif answer!= sol:
            print("wrong")
    except ValueError:
        print("it is not a nunmber")

    