class Viajero():
    __Nombre=""
    __Apellido=""
    __DNI=""
    __num_viajero=int
    __millas_acum=int
    
    def __init__(self,nombre,apellido,dni,num_viajero,millas_acum):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas_acum
    def __str__(self):
        return self.__nombre
    #def CantidadTotalMillas(self):
        #print ('\nla cantidad de millas acumuladas son: %s', str())
    #def AcumularMillas(self, millas=int):
    #    i=self.__millas_acum+millas
    #    return i
    #def CanjearMillas(self, Canjearmillas=int):
    #    if (self.__millas_acum>=Canjearmillas):
    #        print ('\nse canjearon las millas')
    #    else: print ('\nno se canjearon')