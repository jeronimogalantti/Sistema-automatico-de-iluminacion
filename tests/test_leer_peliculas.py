from funciones import leer_peliculas


def test_leer_peliculas():
    peliculas = leer_peliculas()

    assert len(peliculas) == 10
    assert peliculas[0]["titulo"] == "Relatos salvajes"
    assert peliculas[0]["puntaje"] == 8.1