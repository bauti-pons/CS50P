import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        matches = re.search(r"^(0?1?\d):?([0-5]\d)? (A?P?M) to (0?1?\d):?([0-5]\d)? (A?P?M)$", s)
        if not matches:
            raise ValueError("Invalid time format")

        first_hour = int(matches.group(1))
        first_mins = matches.group(2)
        first_mrdm = matches.group(3)
        second_hour = int(matches.group(4))
        second_mins = matches.group(5)
        second_mrdm = matches.group(6)

        if first_mins == None:
            first_mins = 00
        if first_hour == 12 and first_mrdm == "AM":
            first_hour = 00
        elif first_hour == 12 and first_mrdm == "PM":
            pass
        elif first_mrdm == "PM":
            first_hour = first_hour + 12

        if second_mins == None:
            second_mins = 00
        if second_hour == 12 and second_mrdm == "AM":
            second_hour = 00
        elif second_hour == 12 and second_mrdm == "PM":
            pass
        elif second_mrdm == "PM":
            second_hour = second_hour + 12
    except ValueError:
        raise
    except AttributeError:
        raise ValueError

    return f"{first_hour:02}:{first_mins:02} to {second_hour:02}:{second_mins:02}"


if __name__ == "__main__":
    main()
