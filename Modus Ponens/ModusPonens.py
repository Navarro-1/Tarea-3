def verificar_consecuencia(condicion, condicion_implica_resultado):
    if condicion and condicion_implica_resultado:
        return True
    return False

# Ejemplo en la vida real
tarjeta_valida = True
tarjeta_permite_compra = True

if verificar_consecuencia(tarjeta_valida, tarjeta_permite_compra):
    print("Conclusión: La compra se ha realizado con éxito.")
else:
    print("No se puede completar la compra.")