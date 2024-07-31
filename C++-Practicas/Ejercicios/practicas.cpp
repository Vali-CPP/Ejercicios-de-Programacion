#include <iostream>
#include <vector>

using namespace std;

int main() 
{
  cout << "This computing environment uses:" << endl;
  cout << sizeof(char) << " byte for chars" << endl;
  cout << sizeof(short int) << " bytes for shorts" << endl;
  cout << sizeof(int) << " bytes for ints" << endl;
  cout << sizeof(long int) << " bytes for longs" << endl;
  cout << sizeof(float) << " bytes for floats" << endl;
  cout << sizeof(double) << " bytes for doubles" << endl;
  cout << sizeof(bool) << " byte for bools" << endl;
  cout << sizeof(int *) << " bytes for pointers" << endl;

  std::vector vect {1, 2, 3};

	int *ptr = vect.data();
	int *ptr2 = &vect[0];
	cout << (ptr == ptr2) << endl;
}