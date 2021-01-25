def func():
    return 1
func()
func

def hello():
    return 'Hello!'
hello()
hello

greet = hello
greet()
del hello
hello()
greet()
#############################################################################################################################

def hello(name='Pedro'):
    print('The hello() function has been exectued')
    def greet():
        return '\t This is the greet() func inside hello()'
    def welcome():
        return '\t This is Welcome() inside hello()'
    print(greet())
    print(welcome())

hello()
# welcome() no se puede hacer esto porque esta hecha adentro de la funcion hello, entonces para llamarla solo lo puedo hacer llamando la funcion hello

def hello(name='Pedro'):
    print('The hello() function has been exectued')
    def greet():
        return '\t This is the greet() func inside hello()'
    def welcome():
        return '\t This is Welcome() inside hello()'
    print(' I will return a function')
    if name == 'Pedro':
        return greet
    else:
        return welcome
my_new_func = hello()
print(my_new_func())
my_new_func_otro = hello('Jose')
print(my_new_func_otro())

##########################################################################################################################################
def cool():
    def super_cool():
        return 'I am very cool!'
    return super_cool
some_func = cool()
some_func
some_func()


##########################################################################################################################################
def hello():
    return 'Hi Pedro'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())
other(hello)

##########################################################################################################################################

def new_decorator(original_func):
    def wrap_func():
        print('Some extra code before the original function!')
        original_func()
        print('Some extra code after the original function!')
    return wrap_func

def func_needs_decorator():
    print('I wanto to be decorated!!')
func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)
decorated_func()

##########################################################################################################################################
#en jupyter notebook me funciona pero no se porque en vs no me funciona, en otro momento lo busco
def uno(primera_funcion):
    def elwrap():
        print('codigo antes de la funcion original')
        primera_funcion()
        print('codigo despues de la funcion original')
    return elwrap

@uno
def una_funcion():
    print('yo soy la funcion original')
una_funcion()