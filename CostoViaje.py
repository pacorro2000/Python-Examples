def costoHotel(dias):
    return 140*dias

def costoViajeAvion(ciudad):
    if ciudad == "Charlotte":
        return 183 
    if ciudad == "Tampa":
        return 220 
    if ciudad == "Pittsburgh": 
        return 222
    if ciudad == "Los Angeles":
        return 475

def costoAlquilarAuto(dias):
    cost = dias*40
    if dias >= 7:
        cost -= 50
    elif dias >= 3:
        cost -= 20
    return cost 
    
def costoViaje(ciudad, dias, dineroGastos):
    return costoAlquilarAuto(dias) + costoHotel(dias) + costoViajeAvion(ciudad) + dineroGastos
    

print costoViaje("Los Angeles", 5, 600)
