#! /bin/bash

echo "Buscar directorio = d"
echo "Buscar archivo = f"
read opc

if [ $opc == 'd' ]; then
  : 'El parametro -d nos permite acceder a la informacion de las carpetas que 
  estan en la mismo carpeta en la que esta el script'
  echo "Ingrese el nombre del directorio: "
  read carpeta
  if [ -d $carpeta ]; then
    echo "$carpeta existe y es un directorio"
  else
    echo "Esa mamamada no existe"
  fi

elif [ $opc == 'f' ]; then
  : 'El parametro -f nos permite acceder a la informacion de los archivos que
  estan en la mismo carpeta en la que esta el script'
  echo "Ingrese el nombre del archivo: "
  read archivo
  if [ -f $archivo ]; then
    echo "$archivo existe y es un archivo"
  else
    echo "Esa mamamada no existe"
  fi
fi
