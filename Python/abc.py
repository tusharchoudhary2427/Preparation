# IF __NAME__== ‘__MAIN__’ -> ‘__name__’ evaluates to the name of the module in python from where the program is ran. If the program is ran directly, then __name__ is set to ‘__main__’.

def myFunc():
    print("Hello World!")

if __name__ == "__main__":
    print("We are in the main module")
    myFunc()
    print(__name__)