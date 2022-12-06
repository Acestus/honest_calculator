msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

memory = 0
while True:
    print(msg_0)
    equation = input().split()
    operator = equation[1]
    if "M" in equation[0]:
        x = float(memory)
    else:
        x = float(equation[0])
    if "M" in equation[2]:
        if operator == "/" and memory == 0:
            print(msg_3)
            continue
        y = float(memory)
    else:
        y = float(equation[2])
    operations = ["+", "-", "*", "/"]

    try:
        if operator not in operations:
            print(msg_2)
            continue
        if operator == "/" and y == "0":
            print(msg_3)
            continue
    except ValueError:
        print(msg_1)
        continue
    else:
        if operator == "+":
            print(x + y)
            memory = x + y
        elif operator == "-":
            print(x - y)
            memory = x - y
        elif operator == "*":
            print(x * y)
            memory = x * y
        elif operator == "/":
            print(x / y)
            memory = x / y
        print(msg_4)
        answer = input()
        # Store the result in memory
        if answer == "y":
            print(msg_5)
        else:
            print(msg_5)
            memory = 0
        answer = input()
        # Continue calculations?
        if answer == "n":
            break
        elif answer == "y":
            continue
        else:
            break