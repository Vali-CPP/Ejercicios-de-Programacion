#include <iostream>
#include <vector>


int Collatz(int number){
 if(number % 2 == 0){
   if (number == 1){
    return number;
   } 
   number /= 2;
   Collatz(number);
 }else {
    if (number == 1){
    return number;
   }
   number = 3 * number + 1;
   Collatz(number);
 }
}

main(){
    std::cout << "Ingrese un numero: ";
    int num;
    std::cin >> num;
    Collatz(num);
}