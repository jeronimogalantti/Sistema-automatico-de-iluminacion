from funciones import obtener_puntajes



def test_obtener_puntajes():
    peliculas = [
        {"titulo": "Cars", "puntaje": 7.2},
        {"titulo": "Interstellar", "puntaje": 8.7},
        {"titulo": "Coco", "puntaje": 8.4}
    ]

    resultado = obtener_puntajes(peliculas)

    assert resultado == [7.2, 8.7, 8.4]