from datetime import date
import operator
import inflect
import sys


def main():

    try:
        print(number_to_words(get_difference(input("Date of Birth: "))))

    except EOFError:
        sys.exit("EOFError")
    except ValueError:
        sys.exit("ValueError")
    except TypeError:
        sys.exit("TypeError")


def get_difference(d):
    birth = date.fromisoformat(d)
    today = date.today()
    diff = str(operator.sub(today, birth)).split(" ")

    return int(diff[0]) * 24 * 60


def number_to_words(num):
    p = inflect.engine()
    words = p.number_to_words(num)
    if " and " in words:
        words_list = words.split(" and")
        minutes = ""
        for word in words_list:
            minutes += word
    else:
        minutes = words

    return f"{minutes.capitalize()} minutes"


if __name__ == "__main__":
    main()
    
