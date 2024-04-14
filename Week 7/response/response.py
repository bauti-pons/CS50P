from validator_collection import validators, errors


def main():
    print(email_validation(input("What's your email address? ")))


def email_validation(email):
    try:
        if validators.email(email):
            return "Valid"
        else:
            return "Invalid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
