def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operat = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    calc_off = False
    num1 = float(input("What is your first number?: "))
    for key in operat.keys():
        print(key)

    while not calc_off:
        symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is your next number?: "))
        calc_func = operat[symbol]
        answer = calc_func(num1,num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        y_n = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ")
        if y_n == 'n':
            calc_off = True
            calculator()
        else:
            num1 = answer


calculator()