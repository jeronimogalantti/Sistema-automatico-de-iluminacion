def promedio(notas):
    if not notas:
        return "No hay notas"
    total= 0 
    for nota in notas:
        total = total + nota

    return total / len(notas)

notas_genaro = [4,8,7,6,2,10]
notas_juan = [5,6,3,2]

def aprobo(notas):
    return promedio(notas) >= 6

def estadisticas (notas):
    return {
        "promedio": promedio(notas),
        "maximo": max(notas),
        "minimo": min(notas)
    }

def obtener_dato(pelicula, clave):
    return pelicula.get(clave, "desconocido")


def leer_peliculas():
    archivo = open("tests/peliculas.csv", "r")

    peliculas = []

    next(archivo)

    for linea in archivo:
        linea = linea.strip()
        datos = linea.split(",")

        pelicula = {
            "titulo": datos[0],
            "anio": int(datos[1]),
            "puntaje": float(datos[2]),
            "genero": datos[3]
        }

        peliculas.append(pelicula)

    archivo.close()

    return peliculas


def obtener_puntajes(peliculas):
    puntajes = []

    for pelicula in peliculas:
        puntajes.append(pelicula["puntaje"])

    return puntajes

def ordenar_peliculas(peliculas):
    return sorted(peliculas, key=lambda pelicula: pelicula["puntaje"], reverse=True)