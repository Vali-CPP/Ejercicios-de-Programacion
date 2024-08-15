#! /bin/bash

: 'La palabra clave declare funciona para inicializar una varible, a diferencia de la inicializacion normal, declare nos ayuda a darle propiedades extra a las varibles
como por ejemplo, la capacidad de ser solo de lectura o  escritura.'

#declare -r nombre="Valiant"

#ARREGLOS

nombres=("Valiant" "Jose" "Pepito")
#mostrando todo lo que contiene el arreglo
echo "${nombres[*]}"
#mostrando solo los nombres
echo "${!nombres[*]}"
#mostrando la cantidad de elementos
echo "Cantidad de nombres: ${#nombres[*]}"
#mostrando el ultimo nombre
echo "Ultimo nombre: ${nombres[${#nombres[*]} - 1]}"
#Utilizando un bucle for-each para mostrar todos los elementos de un arreglo
for i in ${nombres[*]}; do
  echo "My name is : $i"
done

#podemos eliminar objetos de un arreglo con la palabra clave unset
unset nombres[1]
echo "${nombres[*]}"

#para aniadri un elemento mediante las siguientes logicas
#utilizando el atajo de la cantidad de elementos para aniadir el nuevo elemento al final
nombres[${#nombres[*]} - 1]='Chucaca'
echo "${nombres[*]}"

#o simplemente usamos el comando
nombres+=('Elemento')

#Para modificar un elemento simplemente asignamos el elemento modificado a la posicion deseada
nombres[1]='Valiente'
