def main():

    names = []

    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except EOFError:
            print()
            break

    output = "Adieu, adieu, to "

    if len(names) == 1:
        print(output + names[0])
    elif len(names) == 2:
        print(output + names[0] + " and " + names[1])
    else:
        for i in range(len(names)):
            if i < len(names) - 1:
                output += names[i]
                output += ", "
            else:
                output += "and "
                output += names[i]
                print(output)


main()
