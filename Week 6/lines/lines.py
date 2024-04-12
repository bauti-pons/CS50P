import sys


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a Python file")
        else:
            try:
                print(python_file(sys.argv[1]))
            except FileNotFoundError:
                sys.exit("Not a Python file")


def python_file(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()

    c = 0
    for line in lines:
        l = line.lstrip()
        if l.startswith("#") == False and len(l) > 0:
            c += 1

    return c

if __name__ == "__main__":
    main()
