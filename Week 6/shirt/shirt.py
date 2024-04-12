import sys, os
from PIL import Image, ImageOps


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        format = [".jpeg", ".jpg", ".png"]
        inp_for = os.path.splitext(sys.argv[1])
        outp_for = os.path.splitext(sys.argv[2])
        if outp_for[1].lower() not in format:
            sys.exit("Invalid output")
        elif inp_for[1].lower() != outp_for[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            edit_photo(sys.argv[1], sys.argv[2])


def edit_photo(input, output):

    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as img:
            input_cropped = ImageOps.fit(img, shirt.size)
            input_cropped.paste(shirt, mask=shirt)
            input_cropped.save(output)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
