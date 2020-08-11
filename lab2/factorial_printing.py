import sys
from factorial import Factorial

if __name__ == "__main__":
    
    input_number = int(sys.argv[1])
    factorial_object = Factorial()
    output = factorial_object.compute(input_number)

    if output == -1 :
        print('Kindly enter a whole number, input format is incorrect')
    elif output == -2 :
        print('Kindly enter a whole number, the current input is a negative integer')
    else :
        print('The factorial of ' + str(input_number) + ' is: ' + str(output))
