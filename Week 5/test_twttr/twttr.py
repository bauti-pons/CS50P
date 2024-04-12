def main():

    i = shorten(input("Input: ").strip())
    print(f"Output: {i}")


def shorten(word):
    to_delete = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    result = ""

    for i in word:
        if i not in to_delete:
            result += i
    return result


if __name__ == "__main__":
    main()
