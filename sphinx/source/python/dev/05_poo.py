# definicion de CLASE **********************************************************
"""
plantilla generica a partir de la cual instanciar objetos
esta plantilla define atributos y metodos tendran los objetos de esa clase
"""
# definicion de CLASE en Python
class MyClass:
    """ Brief: a simple example class """   # docstring
    i = 12345                               # class attribute
    def method_1(self):                     # regular method
        return 'Hola Mundo'

# INSTANCIA de una clase: creacion de un objeto
"""
Un OBJETO es una entidad que agrupa un estado y funcionalidades relacionadas.
El estado del objeto se define a traves de variables llamadas ATRIBUTOS, 
mientras que la funcionalidad se modela a traves de funciones a las 
que se les conoce con el nombre de METODOS del objeto.
"""
x = MyClass() # creacion de un objeto de la clase MyClass

# Acesso a atributos y metodos *************************************************
print(x.i)  # acceso a atributos
print(x.method_1())  # acceso a metodos

# INICIALIZACIÓN DE UNA CLASE (CONSTRUCTOR)*************************************
class Complex:
    """
    Brief: Complex numbers class
    """
    def __init__(self,
                 realpart,
                 imagpart):                 # special method
        """
        Brief: constructor method of the class
        :param realpart: real part of number
        :type realpart: real number
        :param imagpart: imaginary part of number
        :type imagpart: real number
        """
        print("Clase inicializada")
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)

print(x.r, x.i)

# ENCAPSULACIÓN ****************************************************************
class Encapsula:
    def public_method(self):
        print("Has accedido a un método público")

    def __private_method(self):
        print("Has accedido a un método privado")

encapsula_object = Encapsula()
encapsula_object.public_method()
encapsula_object.__private_method()

# HERENCIA SIMPLE **************************************************************
class Animal:
    def comer(self):
        print("Puedo comer")

    def andar(self):
        print('Puedo andar')

class Gato(Animal):
    def maullar(self):
        print('Miau')

objeto_gato = Gato()

objeto_gato.comer()
objeto_gato.andar()
objeto_gato.maullar()

# Multiple inheritance *******************************************************
class A():
    def suma(self,a,b):
        c = a+b
        return c
class B():
    def resta(self,a,b):
        c = a-b
        return c
class C(A,B):
    pass

c_obj = C()
print("Suma es ", c_obj.suma(12,4))
print("La resta es ",c_obj.resta(45,5))

# Multilevel inheritance *****************************************************
class A():
    def sum1(self,a,b):
        c = a+b
        return c
class B(A):
    pass
class C(B):
    pass

c_obj = C()
print("Suma es ", c_obj.sum1(12,4))

# POLIMORFISMO *****************************************************************
class Perro():
    def avanzar(self):
        print('Corriendo')
class Pajaro():
    def avanzar(self):
        print('Volando')

def mover(animal):
    animal.avanzar()

objeto_perro = Perro()
objeto_pajaro = Pajaro()

mover(objeto_perro)
mover(objeto_pajaro)