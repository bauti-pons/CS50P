def main():

    x, y, z = input("Expression: ").split(" ")

    if y == "+":
        print(round(float(int(x) + int(z)), 1))
    elif y == "-":
        print(round(float(int(x) - int(z)), 1))
    elif y == "*":
        print(round(float(int(x) * int(z)), 1))
    else:
        print(round(float(int(x) / int(z)), 1))

main()
