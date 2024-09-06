
# Parte 1: Cargar los datos
def cargar_datos(lineas_archivo):
    datos_peliculas = []
    # Ordenar las lineas en peliculas y sus datos
    for linea in lineas_archivo:
        datos_peliculas.append(linea.split(","))
    # print(datos_peliculas)
    # Crear una lista con todos los generos de peliculas
    genero_peliculas = []
    for pelicula in datos_peliculas:
        genero_peliculas.append(pelicula[4])
    # Quitar separacion (;) a las listas de generos creadas
    generos_spliteados = []
    for generos in genero_peliculas:
        generos_spliteados.append(generos.split(";"))
    generos_spliteados2 = []
    # Crear una lista con los distintos generos de peliculas sin repetir
    for generos in generos_spliteados:
        for genero in generos:
            generos_spliteados2.append(genero)
    generos_peliculas = list(set(generos_spliteados2))  # ENUNCIADO
    # ['Drama', 'Comedy', 'Adventure', 'Music', 'Fantasy', 'Action', 'History', 'Animation', 'Thriller', 'Romance', 'Family', 'Western', 'Horror', 'Mystery', 'War', 'Science Fiction', 'Crime']
    # Crear un diccionario con peliculas y sus respectivos generos:
    # Crear una lista con todas las peliculas
    nombre_peliculas = []
    for pelicula in datos_peliculas:
        nombre_peliculas.append(pelicula[0])
    # Crear el diccionario
    listas_generos = {f"{genero.replace(' ', '_')}": []
                      for genero in generos_peliculas}
    dict_pelicula_generos = dict(zip(nombre_peliculas, generos_spliteados))
    # print(dict_pelicula_generos)
    for pelicula, generos in dict_pelicula_generos.items():
        for genero in generos:
            genero_key = f"{genero.replace(' ', '_')}"
            if genero_key in listas_generos:
                listas_generos[genero_key].append(pelicula)
    peliculas_por_genero = [(genero, pelicula)  # ENUNCIADO
                            for genero, pelicula in listas_generos.items()]

    # popularidad = []
    # votos_promedio = []
    # cantidad_votos = []
    # for nota in datos_peliculas:
    #     popularidad.append(nota[1])
    # for votos in datos_peliculas:
    #     votos_promedio.append(votos[2])
    # for cantidad in datos_peliculas:
    #     cantidad_votos.append(cantidad[3])

    # return peliculas_por_genero, generos_peliculas


print(cargar_datos)
# for pelicula, genero in dict_pelicula_generos.items():
#     for genero in generos_peliculas:

# if "Drama" in genero:
#     drama_list.append(pelicula)
# elif "Comedy" in genero:
#     comedy_list.append(pelicula)
# elif "Adventure" in genero:
#     adventure_list.append(pelicula)
# elif "Music" in genero:
#     music_list.append(pelicula)
# elif "Fantasy" in genero:
#     fantasy_list.append(pelicula)
# elif "Action" in genero:
#     action_list.append(pelicula)
# elif "History" in genero:
#     history_list.append(pelicula)
# elif "Animation" in genero:
#     animation_list.append(pelicula)
# elif "Thriller" in genero:
#     thriller_list.append(pelicula)
# elif "Romance" in genero:
#     romance_list.append(pelicula)
# elif "Family" in genero:
#     family_list.append(pelicula)
# elif "Western" in genero:
#     western_list.append(pelicula)
# elif "Horror" in genero:
#     horror_list.append(pelicula)
# elif "Mystery" in genero:
#     mystery_list.append(pelicula)
# elif "War" in genero:
#     war_list.append(pelicula)
# elif "Science Fiction" in genero:
#     science_fiction_list.append(pelicula)
# elif "Crime" in genero:
#     crime_list.append(pelicula)

# print(adventure_list)

# titulo = []
# popularidad = []
# voto_promedio = []
# cantidad_votos = []
# generos = []
# for linea in lineas_archivo:
#     datos_peliculas.append(linea.split(","))
# for nota in datos_peliculas:
#     popularidad.append(nota[1])
# for votopromedio in datos_peliculas:
#     voto_promedio.append(votopromedio[2])
# for cantidadvotos in datos_peliculas:
#     cantidad_votos.append(cantidadvotos[3])
# for genero in datos_peliculas:
#     generos.append(genero[4])

# Parte 2: Completar las consultas


def obtener_puntaje_y_votos(nombre_pelicula):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    pass


def filtrar_y_ordenar(genero_pelicula):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    # Completar con lo que falta aquí
    pass


def obtener_estadisticas(genero_pelicula, criterio):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    # Completar con lo que falta aquí
    pass


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
