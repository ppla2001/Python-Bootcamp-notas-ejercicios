def add(n1,n2):
    print(n1+n2)
add(10,20)
number1 = 10
number2 = input('Please enter a number:')
add(number1,number2)

try:
    result = 10 + '10'
except:
    print('looks like you are not adding correctly!')
else:
    print('add went well!')
    print(result)


result

try:
    f= open('testfile','r')
    f.write('Write a test line')
except TypeError:
    print('there was a type error')
except OSError:
    print('Hey you have an OS Error')
finally:
    print('I always run')

def ask_for_int():
    try:
        result = int(input('Please provide number: '))
    except:
        print('Whoops thats not a number')
    finally:
        print('end of try/except/finally')

ask_for_int()

#para darle mas vueltas al de arriba, te va a seguir preguntando por un numero 
def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops thats not a number')
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print('end of try/except/finally')
            print('I will always run at the end')
            print('Im going to ask you again! \n')

ask_for_int()