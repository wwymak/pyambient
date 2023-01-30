import cppyy
import os


bspline_path, filename = os.path.split ( __file__ )

# this is where we tell cppyy to look for include files and shared libs

cppyy.add_include_path ( bspline_path )
cppyy.add_library_path ( bspline_path )
cppyy.include('FastNoiseLite.h' )
cppyy.include('perlin.cpp')