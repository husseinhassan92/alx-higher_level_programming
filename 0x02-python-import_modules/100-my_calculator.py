#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argv[2]
    func = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in func.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        print("{} {} {} = {}".format(a, operator, b, func[operator](a, b)))
