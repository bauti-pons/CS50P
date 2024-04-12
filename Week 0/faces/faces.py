def main():

    string = input("Enter the word/ phrase: ")
    print(convert(string))

def convert(s):

    s_final = s.replace(":)", "🙂").replace(":(", "🙁")
    return s_final

main()

