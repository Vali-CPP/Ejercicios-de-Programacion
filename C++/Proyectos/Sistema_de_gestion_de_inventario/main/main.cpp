#include <iostream>
#include <cstdlib>
#include "classes.h"
#include "functions.h"

using namespace std;

int main (){
  Inventario Master;
  bool flag = true;
  int op = 0;
  do {
    int op = mostrarMenu();
  switch (op){
   case 1:
    Master.ver();
    break;
   case 2:
    Master.agregar(obtenerNombre(), obtenerPrecio(), obtenerStock());
    break;
   case 3:
     Master.eliminar(obtenerNombre());
     break;
   case 4:
     Master.buscar(obtenerNombre());
     break;
    case 5:
    flag = false;
      break;
    default:
      cout << "Opcion no valida" << endl;
      break;
    }
  system("clear");
  } while (flag);
  return 0;
}
