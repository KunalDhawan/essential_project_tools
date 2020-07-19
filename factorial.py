class Factorial:

    def __init__(self):
        pass

    def compute(self, input_number):

        #First lets perform data validation
        if (isinstance(input_number, int) == 0 ):
            #raise ValueError('Please enter an integer') # Not using ValueError so as to avoiud my app quiting in between if value is incorrect, rather will handle it in upper layer
            print('Please enter an integer')
            return -1

        elif input_number < 0:
            #raise ValueError('Please input a non-negative number. The number entered was: {}'.format(n))
            print('Please input a non-negative number. The number entered was: {}'.format(input_number))
            return -2

        #Defining the recursion base-case 
        elif input_number == 0:
            return 1

        #Defining the recursion
        else:
            return input_number * self.compute( input_number - 1 )