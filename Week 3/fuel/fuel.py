def main():

    print(f"{fuel_per()}", end="")


def fuel_per():

    while True:
        try:
            fraction = input("Fraction: ")
            x = ""
            y = ""
            c = 0
            for i in fraction:
                if i == "/":
                    c += 1
                elif c == 1:
                    y += i
                elif c == 0:
                    x += i
            x_int = int(x)
            y_int = int(y)
            if x_int <= y_int:
                per = x_int / y_int * 100
            f_per = round(per)
            if f_per == 99 or f_per == 100:
                return "F"
            elif f_per == 0 or f_per == 1:
                return "E"
            else:
                return str(f_per) + "%"
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except TypeError:
            pass
        except UnboundLocalError:
            pass


main()
