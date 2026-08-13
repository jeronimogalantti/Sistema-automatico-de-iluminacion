# Sistema automático de iluminación

## Mini-proyecto H1

Este proyecto incluye un programa en Python que lee información de películas desde un archivo CSV, obtiene sus puntajes, calcula estadísticas y muestra las películas ordenadas por puntaje.

## Requisitos

* Python 3
* pytest

Para instalar pytest:

bash
pip install pytest


## Ejecutar el programa

Desde la carpeta raíz del repositorio, ejecutar:

bash
python tests/parteH.py


El programa:

* Lee las películas desde peliculas.csv.
* Obtiene los puntajes de las películas.
* Calcula el promedio, el puntaje máximo y el puntaje mínimo.
* Ordena las películas por puntaje de mayor a menor.
* Muestra los resultados por pantalla.

## Ejecutar los tests

Desde la carpeta raíz del repositorio, ejecutar:

bash
pytest


Los tests verifican el funcionamiento de las funciones utilizadas para calcular las estadísticas de los puntajes.