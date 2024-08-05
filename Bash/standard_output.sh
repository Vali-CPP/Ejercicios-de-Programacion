#! /bin/bash

: 'El stdout o standard output es la salida que muestra un comando al ejecutarlo
como puede ser el ls y demas, es necesario utilizarlo cuando queremos que nuestro programa
nos muestre algo, como un mensaje de succes o de error, el stdout es representado con un 1> despues de un comando, el stdout con un 2> despues de un comando, despues de ingresar estos parametros, tenemos que darles una archivo donde van a escribir '

: 'Aqui estamos ejecutando el comando ls y con el stadndard output estamo
ingresando lo que devuelva en un archivo .txt'
#ls 1>archivo.txt

: 'Ahora estamos mostrando en consola lo que hay en ese archivo con el comando
cat, el cual lee todo lo del archivo .txt y lo muestra en consola'
#cat <archivo.txt

: 'En esta linea, aparte del stdout estaremos tambien utilizando el comando stderr
se utiliza para mostrar cuando un comnado termina con un mensaje
de error o algo parecido, lop guardaremos en un archivo llamado errores.txt por
comodidad'
#ls 1>archivo.txt 2>archivo_errores.txt

: 'tambien tenemos esta forma de escribirlo para no tener escribir tanto'
#ls >archivo.txt >archivo_errores.txt

: 'podemos usar un referenciador para escribirlo todo
en un mismo archivo'
#ls >archivo.txt >&1

: 'Tambien podemos usar esta sintaxis para guardarlo todo en el mismo archivo'
#ls >& archivo.txt
