# Proyecto del Día 7

# Primero vas a crear una clase llamada Persona, y Persona va a tener solo dos atributos:
# nombre y apellido.

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

#  Luego, vas a crear una segunda clase llamada Cliente, y Cliente va a heredar de Persona, porque los clientes son personas, por lo que el Cliente va a heredar entonces los atributos de Persona, pero también va a tener atributos propios, como número de cuenta y balance, es decir, el saldo que tiene en su cuenta bancaria.

class Cliente(Persona):
    def __init__(self, nombre, apellido,numero_cuenta,balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta=numero_cuenta
        self.balance=0.0

# Pero eso no es todo: Cliente también va a tener tres métodos. El primero va a ser uno de los métodos especiales y es el que permite que podamos imprimir a nuestro cliente. Este método va a permitir que cuando el código pida imprimir Cliente, se muestren todos sus datos, incluyendo el balance de su cuenta. 

    def __str__(self):
        return f"""
 _________________________________________________________________________________       
| DATOS ACTUALIZADOS DEL CLIENTE :
|      
| Nombre : {self.nombre}                        
| Apellido : {self.apellido}                    
| Numero de cuenta : {self.numero_cuenta}       
| Balanace : {self.balance}                     
|_________________________________________________________________________________
    """

# Luego, un método llamado Depositar, que le va a permitir decidir cuánto dinero quiere agregar a su cuenta.

    def depositar(self,ingreso):
        ingreso=float(input("Indique el monto a depositar : "))
        self.balance+=ingreso
        return print(usuario.__str__())    
        
# Y finalmente, un tercer método llamado Retirar, que le permita decidir cuánto dinero quiere sacar de su cuenta.

    def retirar(self,retiro):
        retiro=float(input("Indique el monto a retirar : "))
        if retiro>self.balance:
            print(""" 
            Fondos insuficientes.
                """)
        else:
            self.balance-=retiro
        return print(usuario.__str__())

# Una vez que hayas creado estas dos clases, tienes que crear el código para que tu programa se desarrolle, pidiéndole al usuario que elija si quiere hacer depósitos o retiros. El usuario puede hacer tantas operaciones como quiera hasta que decida salir del programa. Por lo tanto, nuestro código tiene que ir llevando la cuenta de cuánto dinero hay en el balance, y debes procurar, por supuesto, que el cliente nunca pueda retirar más dinero del que posee. Esto no está permitido.

def inicio(opcion):
    """menu de opciones."""
    print(usuario.__str__())
    while True:
        opcion=input("""    Menu :
                 
    1- ingresar dinero.
    2- retirar dinero.
    3- salir.
    
Por favor , seleccione una opcion :  """)
        match opcion:             
            case "1": 
                usuario.depositar(ingreso=float)
            case "2":
                usuario.retirar(retiro=float)
            case "3":
                print("Saliendo del programa...")
                break
            case _:
                print("""
                Seleccion invalida , por favor , ingrese una opcion nuevamente.
                      """)
                continue

usuario=Cliente("Mauro","Biasizzo",23564635429732,1200)
inicio(opcion=input)
