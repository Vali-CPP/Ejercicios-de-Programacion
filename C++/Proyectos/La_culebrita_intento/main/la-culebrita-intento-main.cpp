#include <iostream>
#include <unistd.h>
#include <cstdlib>
#include "classes.h"
#include <vector>



//TODO
//-Poner el tablero-
//-Dibujar al Jugador-
//Hacer que el jugador se mueva
//-Poner los limites-
//
//

using namespace std;

int main() {
//Jugador
int pos_x = 1, pos_y = 1;
auto simbolo = '*';

//Tablero
 tablero tablero;

 //game-loop
 while (true) {
   tablero.dibujar();
   tablero.reiniciar();
   tablero.modificar(pos_x++, pos_y++, simbolo);
   sleep(1); 
   if (pos_x == 8) {
     pos_x = 1;
   }else if (pos_y == 11) {
     pos_y = 1;
   }else if (pos_x == 0) {
     pos_x = 8;
   }else if (pos_y == 0) {
     pos_y = 10;
   }
   system("clear");

 }
    return 0;
}
