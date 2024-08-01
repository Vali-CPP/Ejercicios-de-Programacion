#include <iostream>
#include <stdexcept>
#include <limits.h>

int pedir_numero(){
  int number;
  try{
 std::cout << "Ingrese un numero: ";
 std::cin.ignore();
  std::cin >> number;
  if(std::cin.fail()){
    throw std::runtime_error("El dato ingresado debe ser un entero.");
  }}
  catch(const std::runtime_error& e)
  {
    std::cout << "El dato ingresado debe ser un numero entero. \n";
    std::cin.clear();
    std::cin.ignore();
    pedir_numero();
  }
  return number;
}

int Collatz(int number){
 if(number % 2 == 0){
   if (number == 1){
    return number;
   } 
   number /= 2;
   std::cout << number << '\n';
   Collatz(number);
 }else {
    if (number == 1){
    return number;
   }
   number = 3 * number + 1;
   std::cout << number<< '\n';
   Collatz(number);
 }
 return -1;
}

int main(){
    Collatz(pedir_numero()); 
    return 0;
}