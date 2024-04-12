import sys
import csv


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            try:
                headers, students = fix_csv(sys.argv[1])
                get_csv(headers, students, sys.argv[2])
            except FileNotFoundError:
                sys.exit("File does not exist")


def fix_csv(old_file):

    students = []
    n_students = []
    n_headers = ["first", "last", "house"]

    with open(old_file) as o_file:
            reader = csv.reader(o_file)
            headers = next(reader)

    with open(old_file) as o_file:
        dict_reader = csv.DictReader(o_file)

        for row in dict_reader:
            students.append({headers[0]: row[headers[0]], headers[1]: row[headers[1]]})

    for student in students:
        first = ""
        last = ""
        c = 0
        for i in student[headers[0]]:
            if i == ",":
                c = 1
            else:
                if c == 0:
                    last += i
                else:
                    first += i
        first = first.strip()
        last = last.strip()
        n_students.append({n_headers[0]: first, n_headers[1]: last, n_headers[2]: student[n_headers[2]]})

    return n_headers, n_students


def get_csv(headers, students, name):

    with open(name, 'w', newline='') as n_file:
        writer = csv.DictWriter(n_file, fieldnames=headers)
        writer.writeheader()
        
        for student in students:
            writer.writerow({headers[0]: student[headers[0]], headers[1]: student[headers[1]], headers[2]: student[headers[2]]})


if __name__ == "__main__":
    main()
