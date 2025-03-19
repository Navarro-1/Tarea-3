def verificar_negacion(consecuencia, regla_implicacion):
    if not consecuencia and regla_implicacion:
        return False  # Se niega la causa
    return True  # No se puede concluir nada

# Ejemplo en la vida real
alarma_sonando = False
robo_activa_alarma = True

if not verificar_negacion(alarma_sonando, robo_activa_alarma):
    print("Conclusión: No ha habido un robo.")
else:
    print("No se puede determinar con certeza.")