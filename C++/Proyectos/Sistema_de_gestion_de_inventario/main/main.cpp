#include <iostream>
#include <cstdlib>
#include "classes.h"
#include "functions.h"

using namespace std;

int main (){
  Inventario Master;
  int op = 0;
  do {
    int op = mostrarMenu();
  switch (op){
    case 1:
      system("clear");
      Master.ver();
      break;
//   case 2:
//     Master.agregar();
//     break;
//   case 3:
//     Master.eliminar();
//     break;
//   case 4:
//     Master.buscar();
//     break;
    case 5:
      break;
    default:
      system("clear");
      cout << "Opcion no valida" << endl;
      break;
    }
  } while (op != 5);
  return 0;
}
