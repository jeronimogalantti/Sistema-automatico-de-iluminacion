# Notas sobre MQTT

## Pub/sub
En MQTT, un dispositivo publica mensajes en un topic. Otros dispositivos pueden suscribirse a ese topic para recibir los mensajes. El que publica no necesita conocer quiénes están escuchando.

## Broker
Es el componente que recibe los mensajes publicados y los distribuye a los suscriptores correspondientes.

## Topic
Es el nombre jerárquico que identifica el tipo o ubicación del mensaje. Por ejemplo:
`casa/cocina/temperatura`.

## Wildcards
Los wildcards permiten suscribirse a varios topics.
`+` representa un solo nivel y `#` representa todos los niveles restantes.

## ¿Por qué MQTT en lugar de polling?
Con polling, cada sensor o cliente pregunta periódicamente si hay novedades, incluso cuando no hay cambios. Con MQTT, los dispositivos publican cuando tienen información nueva y el broker la distribuye a los suscriptores. Esto evita muchas consultas repetidas cuando hay muchos sensores.