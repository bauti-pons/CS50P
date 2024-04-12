import random
import sys


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        error = 0  # Reset error count for each new problem

        while error < 3:
            try:
                result = int(input(f"{x} + {y} = "))
                if x + y == result:
                    score += 1
                    break  # Correct answer, move to the next problem
                else:
                    error += 1
                    print("EEE")
            except ValueError:
                error += 1
                print("EEE")

            if error == 3:
                print(f"{x} + {y} = {x+y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                raise ValueError  # Ensure that only levels 1, 2, or 3 are acceptable
        except ValueError:
            pass  # The loop will continue, prompting the user again
        except EOFError:
            print()
            sys.exit()


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, or 3.")
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
