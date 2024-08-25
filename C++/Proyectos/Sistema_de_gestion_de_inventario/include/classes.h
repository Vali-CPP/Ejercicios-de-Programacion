#include <iostream>

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

  int getNumero_de_productos(){
    return numero_de_productos;
  }

  void agregar(std::string nom, float price, int stk){
    inventario[getNumero_de_productos()].setNombre(nom);
    inventario[getNumero_de_productos()].setPrecio(price);
    inventario[getNumero_de_productos()].setStock(stk);
    numero_de_productos++;
  }

  void ver(){
    std::cout << "Listado de productos: \n";
    for(int i = 0; i < 10; i++){
      if (inventario[i].getNombre() != "") {
      std::cout << "Nombre: " << inventario[i].getNombre() << "\t Precio: " << inventario[i].getPrecio() << "\t Stock: " << inventario[i].getStock() << "\n";
      }
    }
  }

  void eliminar(std::string nom){
    for (int i = 0; i < 10; i++) {
      if (inventario[i].getNombre() == nom) {
        inventario[i].setNombre("");
        inventario[i].setPrecio(0);
        inventario[i].setStock(0);
      }
    }
     --numero_de_productos;
  }

  void buscar(std::string nom){
    for(int i = 0; i < 10; i++){
      if (inventario[i].getNombre() == nom) {
        std::cout << inventario[i].getNombre() << inventario[i].getPrecio() << inventario[i].getStock() << "\n";
      }
    }
  }
};
