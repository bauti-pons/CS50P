import sys
import csv
from tabulate import tabulate


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            try:
                print(csv_file(sys.argv[1]))
            except FileNotFoundError:
                sys.exit("File does not exist")


def csv_file(file_name):

    table = []
    f_table = []

    with open(file_name) as file:
        reader = csv.reader(file)
        headers = next(reader)

    with open(file_name) as file:
        dict_reader = csv.DictReader(file)
        for row in dict_reader:
            table.append({headers[0]: row[headers[0]], headers[1]: row[headers[1]], headers[2]: row[headers[2]]})

    for dic in table:
        f_table.append([dic[headers[0]], dic[headers[1]], dic[headers[2]]])

    return tabulate(f_table, headers, tablefmt="grid")


if __name__ == "__main__":
    main()
