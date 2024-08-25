#include <iostream>

using namespace std;


class tablero {
  private:
    char tablero[9][12] = {
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
        for (int i = 0; i < 9; i++) {
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