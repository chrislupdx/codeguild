operation = ''
while operation != "done":

    print( "\n add \n subtract \n multiply \n divide \n")
    operation = input(': ')
    if operation != 'done':
        first = int(input('first number?'))
        last = int(input('last number?'))

    if operation == "add":
        addition = input(first + last)
        print(addition)

    elif operation == "multiply":
        multiply = input(int(first) * int(last))
        print(multiply)

    elif operation == "subtract":
        subtraction = input(int(first) - int(last))
        print(subtraction)

    elif operation == "divide":
        division = input(int(first) / int(last))
        print(divide)
