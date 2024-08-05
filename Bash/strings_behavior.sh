echo "Enter ein password"
read input1

echo "Confirm password"
read input2

if [ $input1 == $input2 ]; then
  echo "valido"
else
  echo "Invalido"
fi
