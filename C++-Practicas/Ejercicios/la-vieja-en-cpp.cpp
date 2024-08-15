#include <iostream>
#include <vector>

void mostrarTabla(char *tabla){
  std::cout << *(tabla+0) << "|" << *(tabla+1) << "|" << *(tabla+2) << std::endl;

  std::cout << "-----" << std::endl;

  std::cout << *(tabla+3) << "|" << *(tabla+4) << "|" << *(tabla+5) << std::endl;

  std::cout << "-----" << std::endl;
  
  std::cout << *(tabla+6) << "|" << *(tabla+7) << "|" << *(tabla+8) << std::endl;

  std::cout << "\n";

}

bool comprobarGanador(char *tabla){
  for (int  i = 0; i < 9; i+=3){
    if (*(tabla+i) == *(tabla+i+1) && *(tabla+i+1) == *(tabla+i+2)){
      return true;
    }
  }

   for (int  i = 0; i < 3; i++){
     if (*(tabla+i) == *(tabla+i+3) && *(tabla+i+3) == *(tabla+i+6)){
      return true;
    }
  }

   if (*(tabla+0) == *(tabla+4) && *(tabla+4) == *(tabla+8)){
      return true;
    }

   if (*(tabla+2) == *(tabla+4) && *(tabla+4) == *(tabla+6)){
      return true;
    }

   return false;

  }



int main (){

  char tabla[9] = {'1','2','3','4','5','6','7','8','9'}; 
  int turno = 0;

  while (true and turno++ < 9) {

    std::cout<< "\t\n TURNO DE X \n";
    mostrarTabla(tabla);
    std::cout << "Ingrese la posicion en donde desea colocar X: ";
    int posicion;
    std::cin >> posicion;
    if (posicion - 1 < 0 || posicion - 1 > 8 || tabla[posicion - 1] == 'X' || tabla[posicion - 1] == 'O') {
      std::cout << "\tPOSICION INVALIDA, TURNO PERDIDO \n";
    }else {
      tabla[posicion - 1] = 'X';
      if (comprobarGanador(tabla)) {
        mostrarTabla(tabla);
        std::cout << "\tEL GANADOR ES X\n";
        return 0;
      }
    }

    std::cout<< "\t\n TURNO DE O \n";
    mostrarTabla(tabla);
    std::cout << "Ingrese la posicion en donde desea colocar O: ";
    posicion = 0;
    std::cin >> posicion;
    if (posicion - 1 < 0 || posicion - 1 > 8 || tabla[posicion - 1] == 'X' || tabla[posicion - 1] == 'O') {
      std::cout << "\tPOSICION INVALIDA, TURNO PERDIDO \n";
    }else {
      tabla[posicion - 1] = 'O';
      if (comprobarGanador(tabla)) {
        mostrarTabla(tabla);
        std::cout << "\tEL GANADOR ES O\n";
        return 0;
      }
    }
  }

  std::cout << "SE ACABARON LOS TURNOS, DEBE SER UN MAXIMO DE 9 TURNOS \n";

  return 0;
}
