import csv
import os

# Encabezado esperado del archivo CSV
CSV_HEADER = ['nombre', 'poblacion', 'superficie', 'continente']

# ======================== FUNCIONES DE UTILIDAD ========================

def es_entero_positivo(s: str) -> bool:
    """Verifica si una cadena representa un número entero positivo."""
    s_stripped = s.strip()
    return s_stripped.isdigit() and len(s_stripped) > 0


def normalizar_nombre(nombre: str) -> str:
    """Elimina espacios redundantes y capitaliza el nombre."""
    return " ".join(nombre.strip().split()).title()

# ======================== ARCHIVOS CSV ========================

def cargar_csv(ruta: str):
    """Carga los países desde un archivo CSV, validando formato y datos."""
    paises = []
    if not os.path.exists(ruta):
        print(f" Archivo '{ruta}' no encontrado. Se iniciará con lista vacía.")
        return paises

    with open(ruta, newline='', encoding='utf-8') as f:
        lector = csv.reader(f)
        filas = list(lector)

    if len(filas) == 0:
        print(" CSV vacío. Se iniciará con lista vacía.")
        return paises

    encabezado = [c.strip().lower() for c in filas[0]]
    if encabezado != CSV_HEADER:
        print(" Encabezado del CSV inválido. Se esperaba:", ",".join(CSV_HEADER))
        return paises

    for i, fila in enumerate(filas[1:], start=2):
        if len(fila) != 4:
            print(f"Fila {i} inválida: cantidad de columnas incorrecta. Se omite.")
            continue

        nombre, pobl_str, sup_str, continente = [c.strip() for c in fila]

        if nombre == '' or continente == '':
            print(f"Fila {i} inválida: nombre o continente vacío. Se omite.")
            continue

        if not es_entero_positivo(pobl_str) or not es_entero_positivo(sup_str):
            print(f"Fila {i} inválida: población o superficie no numéricas. Se omite.")
            continue

        pais = {
            'nombre': normalizar_nombre(nombre),
            'poblacion': int(pobl_str),
            'superficie': int(sup_str),
            'continente': continente.title()
        }
        paises.append(pais)

    print(f" Carga finalizada. Países válidos cargados: {len(paises)}")
    return paises


def guardar_csv(ruta: str, paises):
    """Guarda la lista de países en el archivo CSV."""
    with open(ruta, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(CSV_HEADER)
        for p in paises:
            escritor.writerow([p['nombre'], p['poblacion'], p['superficie'], p['continente']])
    print(f" Cambios guardados correctamente en '{ruta}'.")

# ======================== OPERACIONES PRINCIPALES ========================

def existe_pais(paises, nombre: str):
    """Verifica si un país existe (insensible a mayúsculas)."""
    nombre_norm = normalizar_nombre(nombre)
    for idx, p in enumerate(paises):
        if p['nombre'].lower() == nombre_norm.lower():
            return True, idx
    return False, -1


def agregar_pais(paises):
    """Agrega un nuevo país validando todos los campos."""
    print("\n--- Agregar País ---")
    nombre = input("Nombre: ").strip()
    while nombre == '':
        print(" El nombre no puede estar vacío.")
        nombre = input("Nombre: ").strip()

    nombre_norm = normalizar_nombre(nombre)
    existe, _ = existe_pais(paises, nombre_norm)
    if existe:
        print(" Ese país ya existe. Use 'Actualizar país' si desea modificarlo.")
        return

    pobl = input("Población (entero positivo): ").strip()
    while not es_entero_positivo(pobl):
        print(" Población inválida. Ingrese un número entero positivo.")
        pobl = input("Población (entero positivo): ").strip()

    sup = input("Superficie en km² (entero positivo): ").strip()
    while not es_entero_positivo(sup):
        print(" Superficie inválida. Ingrese un número entero positivo.")
        sup = input("Superficie en km² (entero positivo): ").strip()

    continente = input("Continente: ").strip()
    while continente == '':
        print(" El continente no puede estar vacío.")
        continente = input("Continente: ").strip()

    pais = {
        'nombre': nombre_norm,
        'poblacion': int(pobl),
        'superficie': int(sup),
        'continente': continente.title()
    }
    paises.append(pais)
    print(f" País '{pais['nombre']}' agregado con éxito.")


def actualizar_pais(paises):
    """Permite modificar la población y superficie de un país existente."""
    print("\n--- Actualizar País ---")
    nombre = input("Nombre del país a actualizar: ").strip()
    found, idx = existe_pais(paises, nombre)
    if not found:
        print(" País no encontrado.")
        return

    p = paises[idx]
    print(f"Datos actuales: Población={p['poblacion']}, Superficie={p['superficie']}")

    pobl = input("Nueva población (Enter para dejar igual): ").strip()
    if pobl != '':
        while not es_entero_positivo(pobl):
            print(" Valor inválido.")
            pobl = input("Nueva población (Enter para dejar igual): ").strip()
        p['poblacion'] = int(pobl)

    sup = input("Nueva superficie (Enter para dejar igual): ").strip()
    if sup != '':
        while not es_entero_positivo(sup):
            print(" Valor inválido.")
            sup = input("Nueva superficie (Enter para dejar igual): ").strip()
        p['superficie'] = int(sup)

    paises[idx] = p
    print(" Datos actualizados correctamente.")


def buscar_pais(paises):
    """Busca países por nombre parcial o completo."""
    print("\n--- Buscar País ---")
    texto = input("Ingrese texto a buscar: ").strip()
    if texto == '':
        print(" Texto vacío.")
        return
    resultados = [p for p in paises if texto.lower() in p['nombre'].lower()]
    if not resultados:
        print(" No se encontraron coincidencias.")
        return
    print(f" Resultados ({len(resultados)}):")
    for p in resultados:
        print(f"- {p['nombre']}: {p['poblacion']} hab., {p['superficie']} km², {p['continente']}")

# ======================== FILTROS ========================

def filtrar_por_continente(paises):
    """Filtra países por continente ingresado."""
    cont = input("Continente: ").strip().title()
    resultados = [p for p in paises if p['continente'] == cont]
    if not resultados:
        print(" No hay países para ese continente.")
        return
    for p in resultados:
        print(f"- {p['nombre']}: {p['poblacion']} hab., {p['superficie']} km²")


def filtrar_rango_poblacion(paises):
    """Filtra países dentro de un rango de población."""
    print("Ingrese rango de población:")
    min_s = input("Mínima: ").strip()
    max_s = input("Máxima: ").strip()
    if not (es_entero_positivo(min_s) and es_entero_positivo(max_s)):
        print(" Rango inválido.")
        return
    min_v, max_v = int(min_s), int(max_s)
    if min_v > max_v:
        print(" El mínimo no puede ser mayor que el máximo.")
        return
    resultados = [p for p in paises if min_v <= p['poblacion'] <= max_v]
    if not resultados:
        print(" No se encontraron países en ese rango.")
        return
    for p in resultados:
        print(f"- {p['nombre']}: {p['poblacion']} hab.")


def filtrar_rango_superficie(paises):
    """Filtra países por superficie en un rango dado."""
    print("Ingrese rango de superficie (km²):")
    min_s = input("Mínima: ").strip()
    max_s = input("Máxima: ").strip()
    if not (es_entero_positivo(min_s) and es_entero_positivo(max_s)):
        print(" Rango inválido.")
        return
    min_v, max_v = int(min_s), int(max_s)
    if min_v > max_v:
        print(" El mínimo no puede ser mayor que el máximo.")
        return
    resultados = [p for p in paises if min_v <= p['superficie'] <= max_v]
    if not resultados:
        print(" No se encontraron países en ese rango.")
        return
    for p in resultados:
        print(f"- {p['nombre']}: {p['superficie']} km²")

# ======================== ORDENAMIENTOS ========================

def ordenar_paises(paises):
    """Ordena los países según nombre, población o superficie."""
    print("Ordenar por: 1) Nombre  2) Población  3) Superficie")
    op = input("Elija 1/2/3: ").strip()
    if op not in ['1', '2', '3']:
        print(" Opción inválida.")
        return
    asc = input("¿Orden ascendente? (s/n): ").strip().lower() in ['s', 'si']
    if op == '1':
        clave = 'nombre'
    elif op == '2':
        clave = 'poblacion'
    else:
        clave = 'superficie'
    resultados = sorted(paises, key=lambda p: p[clave], reverse=not asc)
    for p in resultados:
        print(f"- {p['nombre']}: {p['poblacion']} hab., {p['superficie']} km²")

# ======================== ESTADÍSTICAS ========================

def mostrar_estadisticas(paises):
    """Calcula máximos, mínimos, promedios y conteo por continente."""
    if not paises:
        print(" No hay datos para calcular estadísticas.")
        return

    mayor = max(paises, key=lambda p: p['poblacion'])
    menor = min(paises, key=lambda p: p['poblacion'])
    promedio_pob = sum(p['poblacion'] for p in paises) / len(paises)
    promedio_sup = sum(p['superficie'] for p in paises) / len(paises)

    print("--- Estadísticas ---")
    print(f" País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f" País con menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f" Promedio de población: {promedio_pob:.2f}")
    print(f" Promedio de superficie: {promedio_sup:.2f} km²")

    continentes = {}
    for p in paises:
        cont = p['continente']
        continentes[cont] = continentes.get(cont, 0) + 1

    print(" Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"- {cont}: {cant} país(es)")

# ======================== MENÚ PRINCIPAL ========================

def menu_principal(paises, ruta_csv):
    """Menú principal interactivo."""
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1) Agregar país")
        print("2) Actualizar país")
        print("3) Buscar país")
        print("4) Filtrar")
        print("5) Ordenar")
        print("6) Estadísticas")
        print("7) Guardar cambios")
        print("8) Salir (sin guardar)")
        print("9) Guardar y salir")

        opcion = input("Elija una opción (1–9): ").strip()
        if opcion == '1':
            agregar_pais(paises)
        elif opcion == '2':
            actualizar_pais(paises)
        elif opcion == '3':
            buscar_pais(paises)
        elif opcion == '4':
            print("Filtros: a) Continente  b) Rango población  c) Rango superficie")
            sub = input("Elija a/b/c: ").strip().lower()
            if sub == 'a':
                filtrar_por_continente(paises)
            elif sub == 'b':
                filtrar_rango_poblacion(paises)
            elif sub == 'c':
                filtrar_rango_superficie(paises)
            else:
                print(" Opción inválida.")
        elif opcion == '5':
            ordenar_paises(paises)
        elif opcion == '6':
            mostrar_estadisticas(paises)
        elif opcion == '7':
            guardar_csv(ruta_csv, paises)
        elif opcion == '8':
            print(" Saliendo sin guardar.")
            break
        elif opcion == '9':
            guardar_csv(ruta_csv, paises)
            print(" Guardado y salida.")
            break
        else:
            print(" Opción inválida.")

# ======================== PROGRAMA PRINCIPAL ========================

def main():
    """Punto de entrada del programa."""
    ruta = 'paises_base.csv'
    paises = cargar_csv(ruta)
    menu_principal(paises, ruta)

if __name__ == '__main__':
    main()
