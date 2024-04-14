import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        direc = re.search(r"^.*<iframe.*https?://(?:www.)?youtube.com/embed/([\w]+).*$", s, re.IGNORECASE)
        if direc:
            return f"https://youtu.be/{direc.group(1)}"
        else:
            return None
    except AttributeError:
        return None


if __name__ == "__main__":
    main()
