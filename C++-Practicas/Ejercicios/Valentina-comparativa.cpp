class contacto {
  public:
    char nombre_completo[50], correo[50], telefono[50], fecha_de_nacimiento[15];
};

int main(){
  contacto contactos[100];
  std::cout << "Ingrese la cantidad de contactos a registrar: ";
  int num_de_contactos=0;
  std::cin >> num_de_contactos;

  for (simplemente haces un for que vaya rellenando cada objeto del arreglo contactos[100] con la informacion a solicitar y asi sucesivamente, ya te explique la logica
      detras de la funcion eliminar, o al menos la que a mi se me ocurrio, y la de editar te recomendaria que primero hicieras una busqueda por el nombre, transformandolo todo a 
      minusculas y comparando strings, la verdad lo importante sera la clase del objeto contacto y no es tan dificil.)
}
