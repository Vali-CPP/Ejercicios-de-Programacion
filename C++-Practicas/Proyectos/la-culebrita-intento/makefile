# Makefile para el proyecto Culebrita

# Compilador
CXX = g++

# Flags del compilador
CXXFLAGS = -Iinclude -Wall -std=c++11

# Archivos fuente
SRC = main/la-culebrita-intento-main.cpp include/classes.h

# Archivo ejecutable
TARGET = culebrita.out

# Regla para compilar todo
all: $(TARGET)

# Regla para crear el ejecutable
$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

# Regla para limpiar los archivos compilados
clean:
	rm -f $(TARGET)
