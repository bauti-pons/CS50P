def main():

    print(f"${value(input("Greeting: "))}")


def value(greeting):

    g = greeting.lower().strip()

    if g[0].isalpha() == False:
        return 100
    elif "hello" in g:
        return 0
    elif g[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
