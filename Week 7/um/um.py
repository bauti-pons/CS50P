import re


def main():
    print(count(input("Text: ").strip()))


def count(s):
    try:
        matches = re.findall(r"\b ?um[\.\.\.]?\??,? ?\b", s, re.IGNORECASE)  # \b ensures the match is a complete word.
        return len(matches)
    except ValueError:
        raise
    except AttributeError:
        raise AttributeError


if __name__ == "__main__":
    main()
