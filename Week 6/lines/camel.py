def main():
    #HELLO
    cc = input("camelCase: ")
    ccf = ""
    for i in cc:
        if i.isupper() == True:
            ccf += "_" + i.lower()
        else:
            ccf += i
    print(ccf)

""""
hola
""""




main()
