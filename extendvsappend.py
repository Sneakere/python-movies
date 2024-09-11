lineas_peliculas = []
with open("movies.csv", "r", encoding="utf-8") as datos:
    for linea in datos.readlines()[1:]:
        lineas_peliculas.append(linea.strip())

genero_pelicula = "War"

lineas_archivo = lineas_peliculas
peliculas_por_genero = {}
generos_peliculas = []
peliculas_segun_genero_extend = []
peliculas_segun_genero_append = []
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
    print(genero, peliculas)
    # Si el genero es igual al argumento entregado en la funcion, se agrega la lista peliculas_segun_genero
    if genero == genero_pelicula:
        peliculas_segun_genero_extend.extend(peliculas)
        print("`````peliculas con extend`````")
        print(f"extend: {peliculas_segun_genero_extend}")
        print("```````````````````````````````")
        print("`````peliculas con append`````")
        peliculas_segun_genero_append.append(peliculas)
        print(f"append: {peliculas_segun_genero_append}")
        print("```````````````````````````````")


# Se reordena segun lo solicitado
peliculas_segun_genero_extend = sorted(
    peliculas_segun_genero_extend, reverse=True)
peliculas_segun_genero_append = sorted(
    peliculas_segun_genero_append, reverse=True)

print("```````````PELICULAS ORDENADAS EXTEND```````````")
print(peliculas_segun_genero_extend)
print("````````````````````````````````````````````````")
print("```````````PELICULAS ORDENADAS APPEND```````````")
print(peliculas_segun_genero_append)
print("````````````````````````````````````````````````")
