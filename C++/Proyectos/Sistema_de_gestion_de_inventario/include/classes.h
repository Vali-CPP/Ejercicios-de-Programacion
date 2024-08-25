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

  public:

  void agregar(int pos, std::string nom, float price, int stk){
    inventario[pos].setNombre(nom);
    inventario[pos].setPrecio(price);
    inventario[pos].setStock(stk);
  }

  void ver(){
    std::cout << "Nombre | Precio | Stock\n";
    for(int i = 0; i < 10; i++){
      if (inventario[i].getNombre() != "") {
      std::cout << inventario[i].getNombre() << inventario[i].getPrecio() << inventario[i].getStock() << "\n";
      }
    }
  }

  void eliminar(int pos){
    inventario[pos].setNombre("");
    inventario[pos].setPrecio(0);
    inventario[pos].setStock(0);
  }

  void buscar(std::string nom){
    for(int i = 0; i < 10; i++){
      if (inventario[i].getNombre() == nom) {
        std::cout << inventario[i].getNombre() << inventario[i].getPrecio() << inventario[i].getStock() << "\n";
      }
    }
  }
};
