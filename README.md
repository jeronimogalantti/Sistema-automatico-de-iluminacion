# Sistema automático de iluminación
CLASE 1:
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

CLASE 2:

API de libros:
Instalación:
Crear y activar el entorno virtual:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

Instalar las dependencias:

pip install -r requirements.txt

Levantar la API
uvicorn ParteB:app --reload

La API queda disponible en:

http://127.0.0.1:8000


Documentación:

http://127.0.0.1:8000/docs


Ejecutar el cliente
Con la API levantada, abrir otra terminal y ejecutar:

python ParteC.py


Ejecutar los tests
pytest -v


Si todo funciona correctamente, los tests deben aparecer como PASSED.


#F3
# 422	
Error: Unprocessable Content

Response body

{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "body",
        "titulo"
      ],
      "msg": "Field required",
      "input": {
        "paginas": 1,
        "editorial": {
          "nombre": "string",
          "pais": "string"
        },
        "disponible": true
      }
    }
  ]
}

# 404
Undocumented
Error: Not Found

Response body
Download
{
  "detail": "Libro no encontrado"
}

# Api apagada
PS C:\IC2\IC2-Equipo\Sistema-automatico-de-iluminacion> python ParteC.py
No se pudo conectar con la API

#F4

Se probaron los mismos pedidos desde /docs y desde curl:

GET /libros
POST válido
POST inválido

En ambos casos se obtuvieron los mismos resultados y códigos HTTP.

Similitud: ambas herramientas permiten enviar solicitudes HTTP a la API y ver la respuesta.

Diferencia: /docs ofrece una interfaz gráfica generada automáticamente por FastAPI, mientras que curl permite hacer las solicitudes directamente desde la terminal.

Para pruebas rápidas durante el desarrollo usaríamos /docs. Para repetir comandos o automatizar pruebas simples, usaríamos curl.