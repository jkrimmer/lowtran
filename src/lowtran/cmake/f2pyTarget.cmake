include(${CMAKE_CURRENT_LIST_DIR}/f2py.cmake)


function(f2py_target module_name module_src out_dir)

set(f2py_bin ${CMAKE_CURRENT_BINARY_DIR}/${module_name}${f2py_suffix})

set(f2py_arg -m ${module_name} -c ${module_src})
if(CMAKE_Fortran_COMPILER_ID MATCHES "^Intel")
  if(WIN32)
    list(APPEND f2py_arg --fcompiler=intelvem)
  else()
    list(APPEND f2py_arg --fcompiler=intelem)
  endif()
endif()

add_custom_command(
OUTPUT ${f2py_bin}
COMMAND ${f2py} ${f2py_arg}
)

add_custom_target(${module_name} ALL DEPENDS ${f2py_bin})

# Install the built Python extension into the wheel/lib directory during
# `cmake --install`, letting the build backend collect it. This avoids copying
# artifacts into the source tree.
if(DEFINED SKBUILD_PLATLIB_DIR)
  set(_dest "${SKBUILD_PLATLIB_DIR}/lowtran")
else()
  # Fallback: install under Python site-packages/lib directory name
  include(GNUInstallDirs)
  set(_dest "${CMAKE_INSTALL_LIBDIR}/lowtran")
endif()

install(FILES ${f2py_bin} DESTINATION ${_dest})

# User-requested: also copy the generated shared library into the source tree
# (out_dir argument) so that `import lowtran7` can find it directly there.
add_custom_command(
  TARGET ${module_name} POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy_if_different ${f2py_bin} ${out_dir}/
  COMMENT "Copying ${f2py_bin} to source directory ${out_dir}"
)

endfunction(f2py_target)
