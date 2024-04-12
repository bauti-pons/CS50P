def main():

    import random
    import sys

    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except TypeError:
            pass
        except ValueError:
            pass
        except EOFError:
            print()
            break

    num = random.randrange(1, level, 1)
    print(num)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < num:
                print("Too small!")
            elif guess > num:
                print("Too large!")
            else:
                sys.exit("Just Right!")
        except TypeError:
            pass
        except ValueError:
            pass
        except EOFError:
            print()
            break


main()
