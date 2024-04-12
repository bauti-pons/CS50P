def main():

    items = {}
    while True:
        try:
            item = input("").strip().upper()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        except EOFError:
                print()
                break
        except SyntaxError:
                pass
        except KeyError:
                pass

    sorted_items = sorted(items)
    for i in range(len(sorted_items)):
        print(items[sorted_items[i]], sorted_items[i])

main()
