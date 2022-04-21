import csv
from Viaje import Viajero

if __name__ == '__main__':
    lista=[]
    archivo = open("Viajantes.csv")
    reader=csv.reader(archivo,delimiter=",")
    total=0
    c=0
    for fila in reader:
        Nombre=fila[0]
        Apellido=fila[1]
        DNI=fila[2]
        num_viajero=fila[3]
        millas_acum=fila[4]
        total=+ int(millas_acum)
        c=+1
        lista.append(Viajero(Nombre,Apellido,DNI,num_viajero,millas_acum))

    
    print ("\nla cantidad de millas acumuladas son: %d", total)
    unViaje=Viajero(Nombre,Apellido,DNI,num_viajero,millas_acum)
    #CantMillas=unViaje.CantidadTotalMillas()
    #print(CantMillas)
    #millas=int(input('\nlas millas realizadas son:'))
    #AcumMillas=unViaje.AcumularMillas(millas)
    #Canjearmillas=int(input('\nla cantidad de millas a canjear son:'))
    #CanjearM=unViaje.CanjearMillas(Canjearmillas)