from funciones import leer_peliculas, obtener_puntajes, estadisticas, ordenar_peliculas


peliculas = leer_peliculas()

puntajes = obtener_puntajes(peliculas)

resultado = estadisticas(puntajes)

peliculas_ordenadas = ordenar_peliculas(peliculas)


print("Estadisticas:")
print("Promedio:", resultado["promedio"])
print("Maximo:", resultado["maximo"])
print("Minimo:", resultado["minimo"])

print("\nPeliculas ordenadas por puntaje:")

for pelicula in peliculas_ordenadas:
    print(pelicula["titulo"], "-", pelicula["puntaje"])