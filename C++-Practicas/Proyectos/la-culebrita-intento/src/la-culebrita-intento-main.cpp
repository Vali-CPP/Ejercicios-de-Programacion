#include <iostream>
#include <unistd.h>
#include <cstdlib>

using namespace std;

class tablero {
  private:
    char tablero[10][12] = {
                            {'-','-','-','-','-','-','-','-','-','-','-','-'},
                            {'|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'},
                            {'|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'},
                            {'|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'},
                            {'|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'},
                            {'|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'},
                            {'|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'},
                            {'|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'},
                            {'-','-','-','-','-','-','-','-','-','-','-','-'}
    };
  public:
    void dibujar() {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 12; j++) {
                cout << tablero[i][j];
            }
            cout << endl;
        }
    }
    void modificar(int x, int y, char simbolo) {
        tablero[x][y] = simbolo;
    }
    void reiniciar() {
        for (int i = 1; i < 8; i++) {
            for (int j = 1; j < 11; j++) {
                tablero[i][j] = ' ';
            }
        }
    }
};

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
   tablero.modificar(pos_x, pos_y, simbolo);
   sleep(1); 
   if (pos_x == 9) {
     break;
   }else if (pos_y == 11) {
     pos_y = 1;
   }
   system("clear");

 }
    return 0;
}
