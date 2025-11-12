cmake_minimum_required(VERSION 3.19...3.26)
# 3.17+ for Python_SOABI

project(lowtran LANGUAGES Fortran)

set(Python3_FIND_VIRTUALENV FIRST)
find_package(Python3 COMPONENTS Interpreter NumPy REQUIRED)
message(STATUS "${PYTHON3_EXECUTABLE}")
message(STATUS "${Python3_NumPy_VERSION}")

enable_testing()

include(cmake/options.cmake)
include(cmake/compilers.cmake)

add_library(lowtran fortran/lowtran7.f)

install(TARGETS lowtran)

include(cmake/f2pyTarget.cmake)

f2py_target(lowtran7 ${CMAKE_CURRENT_SOURCE_DIR}/fortran/lowtran7.f ${CMAKE_CURRENT_SOURCE_DIR})
