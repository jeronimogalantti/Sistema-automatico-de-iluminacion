from funciones import ordenar_peliculas


def test_ordenar_peliculas():
    peliculas = [
        {"titulo": "Cars", "puntaje": 7.2},
        {"titulo": "Interstellar", "puntaje": 8.7},
        {"titulo": "Coco", "puntaje": 8.4}
    ]

    resultado = ordenar_peliculas(peliculas)

    assert resultado[0]["titulo"] == "Interstellar"
    assert resultado[1]["titulo"] == "Coco"
    assert resultado[2]["titulo"] == "Cars"