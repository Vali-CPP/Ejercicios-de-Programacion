#! /bin/bash
echo "Ingresa tu edad: "
read edad

if  (( $edad <=  17 ))
then
	echo "Tu eres un ninio"
else
	echo "Tu ere un duro"
fi
