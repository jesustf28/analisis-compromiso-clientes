"""
PROYECTO: analisis-compromiso-clientes
"""

datos_sesiones = [
    [101, 250, 12],
    [102, 45, 5],
    [103, 120, 7],
    [104, 200, 9],
    [105, 30, 2],
    [106, 90, 4],
    [107, 300, 15]
]

def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

def generar_informe(datos):
    print("=" * 50)
    print("PROYECTO: analisis-compromiso-clientes")
    print("INFORME DE NIVEL DE COMPROMISO")
    print("=" * 50)
    print(f"{'ID Cliente':<15} {'Clasificación':<15}")
    print("-" * 50)
    
    for sesion in datos:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]
        clasificacion = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<15} {clasificacion:<15}")
    
    print("=" * 50)

if __name__ == "__main__":
    print("\n🔄 ANALIZANDO SESIONES...\n")
    generar_informe(datos_sesiones)
    
    altos = sum(1 for s in datos_sesiones if clasificar_compromiso(s[1], s[2]) == "Alto")
    medios = sum(1 for s in datos_sesiones if clasificar_compromiso(s[1], s[2]) == "Medio")
    bajos = sum(1 for s in datos_sesiones if clasificar_compromiso(s[1], s[2]) == "Bajo")
    
    print(f"\n📊 RESUMEN:")
    print(f"  Alto: {altos}")
    print(f"  Medio: {medios}")
    print(f"  Bajo: {bajos}")
    print("\n FIN DE INFORME ")