#include <iostream>
#include "functions.h"

class Producto {
  private:
    std::string nombre;
    float precio;
    int stock;

  public:
    void setNombre(std::string nom){
      nombre = nom;
    };
    void setPrecio(float price){
      precio = price;
    };
    void setStock(int stk){
      stock = stk;
    };
    std::string getNombre(){
      return nombre;
    };
    float getPrecio(){
      return precio;
    };
    int getStock(){
      return stock;
    };
};

class Inventario{
  private:
  Producto inventario[10];
  int numero_de_productos = 0;

  public:

  void setNumero_de_productos(int num){
    numero_de_productos = num;
  }

  int getNumero_de_productos(){
    return numero_de_productos;
  }

bool existeProducto(string nombre) {
  bool flag_existe = false;
    for(int i = 0; i < 10; i++){
      if (inventario[i].getNombre() == nombre) {
        flag_existe = true;
        return flag_existe;
      } 
    }
    return flag_existe; 
}

  int obtenerPosicion(string nom) {
  for (int i = 0; i < 10; i++) {
    if (inventario[i].getNombre() == nom) {
      return i;
    }
  }
  return -1;
  }

  void agregar(std::string nom, float price, int stk){
    inventario[getNumero_de_productos()].setNombre(nom);
    inventario[getNumero_de_productos()].setPrecio(price);
    inventario[getNumero_de_productos()].setStock(stk);
    setNumero_de_productos(getNumero_de_productos() + 1);
    std::cout << "Se ha agregado el producto con exito" << "\n";
  }

  void ver(){
    if (getNumero_de_productos() == 0) {
      std::cout << "No hay productos en el inventario" << "\n";
    } else {
    std::cout << "Listado de productos: \n";
    for(int i = 0; i < getNumero_de_productos(); i++){
      if (inventario[i].getNombre() != "") {
      std::cout << "Nombre: " << inventario[i].getNombre() << "\t Precio: " << inventario[i].getPrecio() << "\t Stock: " << inventario[i].getStock() << "\n";
      }
    }
  }
    Pausa();
}

  void eliminar(std::string nom){
      if (existeProducto(nom)) {
        int pos = obtenerPosicion(nom);
        inventario[pos].setNombre("");
        inventario[pos].setPrecio(0);
        inventario[pos].setStock(0);
        std::cout << "Se ha eliminado el producto con exito" << "\n";
        setNumero_de_productos(getNumero_de_productos() - 1);
      }else {
        std::cout << "No se encontro el producto o el producto no se encuentra en stock" << "\n";
  }
      Pausa();
}

  void buscar(std::string nom){
    if (existeProducto(nom)) {
      int pos = obtenerPosicion(nom);
        std::cout << "Nombre: " << inventario[pos].getNombre() << "\t Precio: " << inventario[pos].getPrecio() << "\t Stock: " << inventario[pos].getStock() << "\n";
      }else {
        std::cout << "No se encontro el producto o el producto no se encuentra en stock" << "\n";
      }
      Pausa();
  }
};
