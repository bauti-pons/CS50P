def main():
    plate = input("Plate: ")
    if is_valid(plate):
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

main()
