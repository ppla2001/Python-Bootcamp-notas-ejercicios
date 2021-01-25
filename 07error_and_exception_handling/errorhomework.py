#1
try:
    for i in ['a','b','c']:
            print(i**2)
except TypeError:
    print('Unexpected Type Error, Please try again!')

#2
try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print('Unexpected ZeroDivisionError, please change division and try again!')
finally:
    print('All Done!')

#3
def ask():
    while True:
        try:
            number = int(input('Please provide a number: ')) 
            square = number ** 2 
        except:
            print('Input an integer: null\nAn error ocurred! Input not a number, try again!\n')
        else:
            print('Input an integer: {}'.format(number))
            print(f'Thank you! Your number is: {square}')
            break

ask()