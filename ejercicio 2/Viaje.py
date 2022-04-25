class Viajero():
    __Nombre=""
    __Apellido=""
    __DNI=""
    __num_viajero=int
    __millas_acum=int
    
    def __init__(self,nombre,apellido,dni,num_viajero,millas_acum):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
        self.__num_viajero=num_viajero
        self.__millas_acum=millas_acum
    
    def __str__(self):
        return str(self.__num_viajero, self.__millas_acum)
    
    def numero(self):
        return self.__num_viajero
    
    def CantidadTotalMillas(self):
        return (self.__millas_acum)
    
    def AcumularMillas(self, millas=int):
        i=self.__millas_acum+millas
        return i
    
    def CanjearMillas(self, acumuladas, canjearmilla=int):
        if (self.__millas_acum>=canjearmilla):
            print ('\nse canjearon las millas')
            acumuladas=acumuladas-canjearmilla
            return (acumuladas)
        else: 
            print ('\nno se canjearon')
            return (acumuladas)