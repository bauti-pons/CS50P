def main():

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                s_date = date.split("/")
                m = s_date[0]
                d = s_date[1]
                y = s_date[2]
                if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
                    print(f"{y}-{m.zfill(2)}-{d.zfill(2)}")
                    break
                else:
                    ValueError
            else:
                s_date = date.split(" ")
                m = str(months.index((s_date[0])) + 1)
                d = s_date[1][:-1]
                y = s_date[2]
                if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
                    print(f"{y}-{m.zfill(2)}-{d.zfill(2)}")
                    break
                else:
                    ValueError

        except SyntaxError:
            pass
        except KeyError:
            pass
        except ValueError:
            pass
        except IndexError:
            pass

main()
