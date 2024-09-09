
# Parte 1: Cargar los datos


def cargar_datos(lineas_archivo):
    # Inicializar estructuras solicitados por el enunciado:
    generos_peliculas = []
    peliculas_por_genero = {}
    info_peliculas = []
    peliculas_por_genero2 = []
    # Iterar por cada linea de lineas archivo y asignar los valores a variables
    for fila in lineas_archivo:
        fila = fila.split(",")
        pelicula = fila[0]
        popularidad = fila[1]
        voto_promedio = fila[2]
        cantidad_votos = fila[3]
        generos = fila[4].split(";")
        # Iterar por cada genero dentro de la variables generos
        for genero in generos:
            # Si genero no esta en generos_peliculas = [], lo agrega a la lista
            if genero not in generos_peliculas:
                generos_peliculas.append(genero)
            # Si genero no esta en el diccionario peliculas_por_genero = {} lo agrega, utilizando de indice el mismo genero encontrado
            if genero not in peliculas_por_genero:
                peliculas_por_genero[genero] = []
            # Agrega la pelicula correspondiente a cada genero en el diccionario creado anteriormente
            peliculas_por_genero[genero].append(pelicula)
        # Se crea la lista info_peliculas con los datos solicitados
        info_peliculas.append([
            pelicula,
            popularidad,
            voto_promedio,
            cantidad_votos,
            generos
        ])
    # Se transforma la lista info_peliculas en una lista de tuplas como se solicita
    info_peliculas = [tuple(pelicula) for pelicula in info_peliculas]
    # Se transforma peliculas_por_genero en una lista de tuplas a partir de un ciclo for que itera en el diccionario creado antes
    for pelicula, genero in peliculas_por_genero.items():
        peliculas_por_genero2.append((pelicula, genero))
    # con return, se entregan las estructuras solicitadas
    return generos_peliculas, peliculas_por_genero2, info_peliculas


# Parte 2: Completar las consultas


def obtener_puntaje_y_votos(nombre_pelicula):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    for fila in lineas_archivo:
        fila = fila.split(",")
        pelicula = fila[0]
        voto_promedio = fila[2]
        cantidad_votos = fila[3]
        # Si la variable asignada a la funcion es igual a la variable pelicula, se guarda su voto promedio y cantidad de votos en una tupla
        if nombre_pelicula == pelicula:
            puntaje_y_votos = (voto_promedio, cantidad_votos)
    # Se entrega la tupla creada
    return puntaje_y_votos


def filtrar_y_ordenar(genero_pelicula):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    peliculas_por_genero = {}
    generos_peliculas = []
    peliculas_segun_genero = []
    for fila in lineas_archivo:
        fila = fila.split(",")
        pelicula = fila[0]
        generos = fila[4].split(";")
        for genero in generos:
            if genero not in generos_peliculas:
                generos_peliculas.append(genero)
            if genero not in peliculas_por_genero:
                peliculas_por_genero[genero] = []
            peliculas_por_genero[genero].append(pelicula)
    # Se recorre el diccionario peliculas_por_genero
    for genero, peliculas in peliculas_por_genero.items():
        # Si el genero es igual al argumento entregado en la funcion, se agrega la lista peliculas_segun_genero
        if genero == genero_pelicula:
            peliculas_segun_genero.extend(peliculas)
    # Se reordena segun lo solicitado
    peliculas_segun_genero = sorted(peliculas_segun_genero, reverse=True)
    # Devuelve la lista generada
    return peliculas_segun_genero


def obtener_estadisticas(genero_pelicula, criterio):

    lineas_archivo = leer_archivo()
    estadisticas = []
    lista_popularidad = []
    lista_voto_promedio = []
    lista_cantidad_votos = []

    for fila in lineas_archivo:
        fila = fila.split(",")
        popularidad = float(fila[1])
        voto_promedio = float(fila[2])
        cantidad_votos = float(fila[3])
        generos = fila[4].split(";")

        # Agrega a una lista todos los valores de un genero segun criterio
        if genero_pelicula in generos:
            lista_popularidad.append(popularidad)
            lista_voto_promedio.append(voto_promedio)
            lista_cantidad_votos.append(cantidad_votos)

    if criterio == "popularidad":
        maximo = max(lista_popularidad)
        minimo = min(lista_popularidad)
        promedio = sum(lista_popularidad)/len(lista_popularidad)
        estadisticas.extend([maximo, minimo, promedio])
        return estadisticas
    elif criterio == "voto promedio":
        maximo = max(lista_voto_promedio)
        minimo = min(lista_voto_promedio)
        promedio = sum(lista_voto_promedio)/len(lista_voto_promedio)
        estadisticas.extend([maximo, minimo, promedio])
        return estadisticas
    else:
        maximo = max(lista_cantidad_votos)
        minimo = min(lista_cantidad_votos)
        promedio = sum(lista_cantidad_votos)/len(lista_cantidad_votos)
        estadisticas.extend([maximo, minimo, promedio])
        return estadisticas

    # NO ES NECESARIO MODIFICAR DESDE AQUI HACIA ABAJO


def solicitar_accion():
    print("\n¿Qué desea hacer?\n")
    print("[0] Revisar estructuras de datos")
    print("[1] Obtener puntaje y votos de una película")
    print("[2] Filtrar y ordenar películas")
    print("[3] Obtener estadísticas de películas")
    print("[4] Salir")

    eleccion = input("\nIndique su elección (0, 1, 2, 3, 4): ")
    while eleccion not in "01234":
        eleccion = input(
            "\nElección no válida.\nIndique su elección (0, 1, 2, 3, 4): ")
    eleccion = int(eleccion)
    return eleccion


def leer_archivo():
    lineas_peliculas = []
    with open("movies.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    return lineas_peliculas


def revisar_estructuras(generos_peliculas, peliculas_por_genero, info_peliculas):
    print("\nGéneros de películas:")
    for genero in generos_peliculas:
        print(f"    - {genero}")

    print("\nTítulos de películas por genero:")
    for genero in peliculas_por_genero:
        print(f"    genero: {genero[0]}")
        for titulo in genero[1]:
            print(f"        - {titulo}")

    print("\nInformación de cada película:")
    for pelicula in info_peliculas:
        print(f"    Nombre: {pelicula[0]}")
        print(f"        - Popularidad: {pelicula[1]}")
        print(f"        - Puntaje Promedio: {pelicula[2]}")
        print(f"        - Votos: {pelicula[3]}")
        print(f"        - Géneros: {pelicula[4]}")


def solicitar_nombre():
    nombre = input("\nIngrese el nombre de la película: ")
    return nombre


def solicitar_genero():
    genero = input("\nIndique el género de película: ")
    return genero


def solicitar_genero_y_criterio():
    genero = input("\nIndique el género de película: ")
    criterio = input(
        "\nIndique el criterio (popularidad, voto promedio, cantidad votos): "
    )
    return genero, criterio


def main():
    lineas_archivo = leer_archivo()
    datos_cargados = True
    try:
        generos_peliculas, peliculas_por_genero, info_peliculas = cargar_datos(
            lineas_archivo
        )
    except TypeError as error:
        if "cannot unpack non-iterable NoneType object" in repr(error):
            print(
                "\nTodavía no puedes ejecutar el programa ya que no has cargado los datos\n"
            )
            datos_cargados = False
    if datos_cargados:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()

            if accion == 0:
                revisar_estructuras(
                    generos_peliculas, peliculas_por_genero, info_peliculas
                )

            elif accion == 1:
                nombre_pelicula = solicitar_nombre()
                ptje, votos = obtener_puntaje_y_votos(nombre_pelicula)
                print(
                    f"\nObteniendo puntaje promedio y votos de {nombre_pelicula}")
                print(f"    - Puntaje promedio: {ptje}")
                print(f"    - Votos: {votos}")

            elif accion == 2:
                genero = solicitar_genero()
                nombres_peliculas = filtrar_y_ordenar(genero)
                print(f"\nNombres de películas del género {genero} ordenados:")
                for nombre in nombres_peliculas:
                    print(f"    - {nombre}")

            elif accion == 3:
                genero, criterio = solicitar_genero_y_criterio()
                estadisticas = obtener_estadisticas(genero, criterio)
                print(
                    f"\nEstadísticas de {criterio} de películas del género {genero}:")
                print(f"    - Máximo: {estadisticas[0]}")
                print(f"    - Mínimo: {estadisticas[1]}")
                print(f"    - Promedio: {estadisticas[2]}")

            else:
                salir = True
        print("\n********** ¡Adiós! **********\n")


if __name__ == "__main__":
    main()
