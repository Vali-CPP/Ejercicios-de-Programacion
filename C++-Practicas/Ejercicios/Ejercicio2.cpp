#include <iostream>

int contar_apariciones(char frase[], char letra) {
  int i = 0, apariciones=0;
  while (frase[i] != '\0') {
    if (frase[i] == letra) {
      apariciones++;
    }
    i++;
  }
  return apariciones;
}

int main () {
  std::cout << "Ingrese su la frase: ";
  char frase[100];
  std::cin.getline(frase, 100);
  std::cout << "Ingrese la primera consonante de su nombre: ";
  char consonante;
  std::cin >> consonante;
  std::cout << "La cantidad de apariciones que tiene la letra " << consonante << " en la frase es de " << contar_apariciones(frase, consonante) << " veces.";
}
