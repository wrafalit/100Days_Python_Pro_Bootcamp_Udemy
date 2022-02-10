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
calc_off = False

while not calc_off:
    num1 = int(input("What is your first number?: "))

    for key in operat.keys():
        print(key)
    symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What is your second number?: "))
    calc_func = operat[symbol]
    firs_answer = calc_func(num1,num2)
    print(f"{num1} {symbol} {num2} = {firs_answer}")
    while not calc_off:
        y_n = input(f"Type 'y' to continue calculation with {firs_answer}, or type 'n' to exit.:  ")
        if y_n == 'n':
            calc_off = True
            break
        symbol = input("Pick an operation from the line above: ")
        calc_func = operat[symbol]
        num3 = int(input("What is your next number?: "))
        sec_answer = calc_func(firs_answer,num3)

        print(f"{firs_answer} {symbol} {num3} = {sec_answer}")
        firs_answer = sec_answer
