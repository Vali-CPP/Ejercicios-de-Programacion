# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles/Ejemplo-1_autogen.dir/AutogenUsed.txt"
  "CMakeFiles/Ejemplo-1_autogen.dir/ParseCache.txt"
  "Ejemplo-1_autogen"
  )
endif()
