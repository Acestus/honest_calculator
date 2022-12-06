msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

print(msg_0)

while True:
    equation = input()
    split_equation = equation.split()
    try:
        float(split_equation[0])
        float(split_equation[2])
        if split_equation[1] not in ["+", "-", "*", "/"]:
            print(msg_2)
            print(msg_0)
            continue
    except ValueError:
        print(msg_1)
        print(msg_0)
        continue
    else:
        break