def calcular_transporte (distancia):
    costo_transporte = distancia * 5 #serían 5 pesos x kilómetro
    return costo_transporte

def calcular_comida(dias, presupuesto_diario=50):
    costo_comida = dias * presupuesto_diario
    return costo_comida

def mostrar_resumen(destino, costo_transporte, costo_comida):
    costo_total = costo_transporte + costo_comida
    msj = (f"En tu viaje con destino a: {destino}, transporte ${costo_transporte}, comida ${costo_comida}, Total${costo_total}")
    return msj

destino_usuario = input("Escribe el destino del viaje: ")

distancia_usuario = int(input("Escribe la distancia en kilómetros por favor: "))

dias_usuario = int(input("Escribe cuántos días dura el viaje: "))

resultado_transporte = calcular_transporte (distancia_usuario)
resultado_comida = calcular_comida (dias_usuario)
resultado_final = mostrar_resumen (destino_usuario, resultado_transporte, resultado_comida)

                   
print(resultado_final)                   


