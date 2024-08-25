#include <iostream>
#include "functions.h"

using namespace std;

int mostrarMenu() {
  cout << "\tBIENVENIDO A SU SISTEMA DE GESTION DE INVENTARIO.\n";
  cout << "Elija una opcion:\n";
  cout << "1. Ver inventario.\n";
  cout << "2. Agregar producto.\n";
  cout << "3. Eliminar producto.\n";
  cout << "4. Buscar producto por nombre.\n";
  cout << "5. Salir.\n";
  cout << "Opcion: ";
  int opcion;
  cin >> opcion;
  return opcion;
}
