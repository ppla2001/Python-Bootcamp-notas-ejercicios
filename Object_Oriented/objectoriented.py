mylist = [1,2,3]

class SampleWord():
    pass

my_sample = SampleWord()
type(my_sample)

class Dog():
    species = 'Mammal' #es siempre lo mismo a pesar de lo q de abajo cambie porq esta arriba del __init__
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots
    
    def bark(self,number):
        print ('Woof my name is {} and the number is {}'.format(self.name,number))

my_dog = Dog(breed='lab',name='Sammy', spots=False)
my_dog.species
my_dog.breed
my_dog.spots
my_dog.bark(17) #a diferencia de los q estan adentro de __init__, los que usan methods (funiones adentro de class), usan ()
type(my_dog)

#otro ejemplo
class Circle():
    pi = 3.14
    def __init__(self, radius=1): #pongo radius = 1 como default, despues cuando llamo la class lo puedo cambiar en ()
        self.radius = radius
        self.area = radius*radius*self.pi  #o Circle.pi
    def get_circumference(self):
        return self.radius * self.pi * 2 
my_circle = Circle(30)
my_circle.pi
my_circle.radius
my_circle.area
my_circle.get_circumference()

#inheritance 
class Animal():
    def __init__(self):
        print('Animal Created')
    def who_am_i(self):
        print('i am an animal')
    def eat(self):
        print('I am eating')
my_animal = Animal()

class Perro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Perro created')
    def who_am_i(self):
        print('Soy un perro') #para cambiar de la otra class y sobreleer con esta
    def bark(self):
        print('Woof!')

my_perro = Perro()
my_perro.who_am_i()
my_perro.eat()
my_perro.bark()

#polimorphism
class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' says woof!'

class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' says meow!'

niko = Dog('niko')
felix = Cat('felix')

niko.speak()
felix.speak()

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))

def pet_speak(pet):
    print(pet.speak())
pet_speak(niko)
pet_speak(felix)

class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')

myanimal = Animal('fred')
myanimal.speak()

class Dog(Animal):
    def speak(self):
        return self.name + ' says woof!'
fido = Dog('fido')
fido.speak()

#special (magic/dunder) method
class Book():
    def __init__(self, title,author,pages):
        self.title = title
        self.author= author
        self.pages= pages
    def __str__(self):
        return f'{self.title} by {self.author} with {self.pages} pages!' 
    def __len__(self):
        return self.pages
    def __del__(self):
        print('A book object has been deleted')

b = Book('Python rocks' , 'Jose' , 200)
print(b)
str(b)
len(b)
del b
print(b)