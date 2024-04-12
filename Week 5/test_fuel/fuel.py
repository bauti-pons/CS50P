def main():

    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        print(e)


def convert(fraction):
    
    try:
        x, y = map(int, fraction.split("/"))
        if x > y:
            raise ValueError("Numerator cannot be greater than the denominator.")
        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
    except ValueError:
        raise ValueError("Invalid input. Both numerator and denominator must be integers.")
    return round(x / y * 100)


def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
