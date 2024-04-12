def main():

    if is_valid(input("Plate: ")):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if s[0:2].isalpha() == False or s.isalnum() == False:
        return False
    if not 2 <= len(s) <= 6:
        return False
    c = 0
    for i in s:
        if i.isalpha() == False:
            if i == "0" and c == 0:
                return False
            c = 1
        elif i.isalpha() == True and c == 1:
            return False
    return True


if __name__ == "__main__":
    main()
