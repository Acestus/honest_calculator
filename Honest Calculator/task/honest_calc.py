def is_one_digit(num):
    return -10 < num < 10 and (int(num) == num or num == 0)

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0

while True:
    print(msg_0)
    msg = ""
    equation = input().split()
    operator = equation[1]
    if "M" in equation[0]:
        x = float(memory)
    else:
        x = float(equation[0])
    if "M" in equation[2]:
        if operator == "/" and memory == 0:
            msg += msg_6
            if msg != "":
                msg = msg_9 + msg
            print(msg)
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
        if is_one_digit(x) and is_one_digit(y):
            msg += msg_6
        if (x == 1 or y == 1) and (operator == "*"):
            msg += msg_7
        if (x == 0 or y == 0) and (operator == "*" or operator == "+" or operator == "-"):
            msg += msg_8
        if msg != "":
            msg = msg_9 + msg
        print(msg)
        if operator == "+":
            print(x + y)
            buffer = x + y
        elif operator == "-":
            print(x - y)
            buffer = x - y
        elif operator == "*":
            print(x * y)
            buffer = x * y
        elif operator == "/":
            print(x / y)
            buffer = x / y
        print(msg_4)
        answer_store = input()
        # Store the result in memory
        if answer_store == "y" and is_one_digit(buffer):
            print(msg_10)
            answer_store = input()
            if answer_store == "y":
                print(msg_11)
                answer_store = input()
                if answer_store == "y":
                    print(msg_12)
                    answer_store = input()
                    if answer_store == "y":
                        print(msg_5)
                        memory = buffer
                    else:
                        print(msg_5)
                else:
                    print(msg_5)
            else:
                print(msg_5)
        elif answer_store == "n" and is_one_digit(buffer):
            print(msg_5)
        if answer_store == "y" and not is_one_digit(buffer):
            print(msg_5)
            memory = buffer
        elif not is_one_digit(buffer):
            print(msg_5)
            buffer = 0
        answer_continue = input()
        # Continue calculations?
        if answer_continue == "n":
            break
        elif answer_continue == "y":
            continue
        else:
            break