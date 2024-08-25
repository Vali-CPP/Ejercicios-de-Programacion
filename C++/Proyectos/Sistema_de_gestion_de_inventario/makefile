# Makefile generico para C++ 

# Compilador
CXX = c++

# Flags del compilador
CXXFLAGS = -Iinclude -Wall -std=c++11

# Archivos fuente
SRC = main/main.cpp include/classes.h include/functions.cpp

# Archivo ejecutable
TARGET = ejecutable.out

# Regla para compilar todo
all: $(TARGET)

# Regla para crear el ejecutable
$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

# Regla para limpiar los archivos compilados
clean:
	rm -f $(TARGET)
