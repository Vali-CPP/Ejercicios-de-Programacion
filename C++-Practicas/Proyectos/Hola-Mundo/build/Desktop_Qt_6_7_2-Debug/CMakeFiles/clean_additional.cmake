# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles/Hola-Mundo_autogen.dir/AutogenUsed.txt"
  "CMakeFiles/Hola-Mundo_autogen.dir/ParseCache.txt"
  "Hola-Mundo_autogen"
  )
endif()
