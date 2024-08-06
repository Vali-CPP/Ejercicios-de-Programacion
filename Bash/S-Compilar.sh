if [ $1 == "c" ]
then
  echo "Ingrese el nombre del archivo a compilar: "
  read compilar
  compilarejecutable="$compilar-ejecutable"
  cpp -o $compilar $compliarejecutable
  1> echo "Compilacion correcta" 2>echo "Compilacion Erronea"
