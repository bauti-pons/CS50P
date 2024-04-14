import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        matches = re.search(r"^([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})$", ip)
        for match in matches.groups():
            if int(match) < 0 or int(match) > 255:
                return False
        return True
    except AttributeError:
        return False


if __name__ == "__main__":
    main()
