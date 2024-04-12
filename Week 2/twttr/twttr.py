def main():

    print(shorten(input("Input: ").strip()))


def shorten(word):
    to_delete = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    result = ""

    for i in word:
        if i not in to_delete:
            result += i
    return f"Output: {result}"


if __name__ == "__main__":
    main()
