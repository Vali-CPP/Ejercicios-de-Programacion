#! /bin/bash

: 'A pesar de haber definido la variable dentro de una funciona, la variable es global, puede ser afectada y se puede acceder a ella desde cualquier parte
del programa, para lograr que solamente sea accesible mediante la funciona se le antepone la palabra clave local'

function di_hola() {
  local message="Hola $1, tienes $2 anios?"
  echo $message
}
#Utilizando la funcion
di_hola "Valiant" 18

: 'Demonstrando como al colocar la varible como local,
podemos podemos reutilizar el nombre en cualquier otra
parte del programa'

message=5
echo $message
