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

string obtenerNombre() {
  cin.ignore();
  cout << "Ingrese el nombre del producto" << endl;
  string nombre;
  getline(cin, nombre);
  return nombre;
}

float obtenerPrecio() {
  cin.ignore();
  cout << "Ingrese el precio del producto" << endl;
  float precio;
  cin >> precio;
  return precio;
}

int obtenerStock() {
  cin.ignore();
  cout << "Ingrese la cantidad en stock del producto" << endl;
  int stock;
  cin >> stock;
  return stock;
}
