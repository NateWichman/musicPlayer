#define Python user-defined exceptions

class CLI_Audio_Exception(Exception):
    """Base class for user-defined exceptions"""
    pass

class WindowToSmall(CLI_Audio_Exception):
    """Raised when the input value is too small"""
    pass

class AudioBlank(CLI_Audio_Exception):
    """Raised when the input value is too large"""
    pass

#Main program
#user guesss number until they get it right

number = 10

if int(input("ENTER: ")) == number:
    print("CORECT")
    print()
print("CHECKPOINT")

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try agian!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try agian!")
        print()

print("Congratulations! You guessed it correctly.")
