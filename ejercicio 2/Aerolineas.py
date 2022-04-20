class Viaje():
    __num_viajero=int
    __dni=''
    __nombre=''
    __apellido=''
    __millas_acum=int
    def __init__(self, num_viajero=int, dni='', nombre='', apellido='', millas_acum=int):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas_acum
    def CantidadTotalMillas(self):
        return '\nla cantidad de millas acumuladas son:'+self.__millas_acum
    def AcumularMillas(self, millas=int):
        i=self.__millas_acum+millas
        return i
    def CanjearMillas(self, Canjearmillas=int):
        if (self.__millas_acum>=Canjearmillas):
            print ('\nse canjearon las millas')
        else: print ('\nno se canjearon')


if __name__ == '__main__':
    unViaje=Viaje()
    CantMillas=Viaje.CantidadTotalMillas()
    millas=int(input('\nlas millas realizadas son:'))
    AcumMillas=Viaje.AcumularMillas(millas)
    Canjearmillas=int(input('\nla cantidad de millas a canjear son:'))
    CanjearM=Viaje.CanjearMillas(Canjearmillas)
