import os


def ag():
    aa = input("Do You Want To Search Again Yes Or No:  ")
    aaa = aa.lower()
    if aaa == "yes":
        check()
    else:
        os.system('clear')
        print('Quiting')



def check():
    os.system('clear')
    f = open("txt.txt", "r")
    a = input('What Do You Want To Search:  ')

    os.system('clear')

    lin = 0
    toaltim = 0
    for line in f:
        lin = lin + 1

        if a in line:
            toaltim = toaltim + 1
            print(f"Found at {lin}, \nContent -> {line}")
    print(f"{a} was found {toaltim} time(s)")
    f.close()
    ag()


check()