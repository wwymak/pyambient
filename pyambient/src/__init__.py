import cppyy
import os


folder_path, filename = os.path.split ( __file__ )

# this is where we tell cppyy to look for include files and shared libs

cppyy.add_include_path ( folder_path )
cppyy.add_library_path ( folder_path )
cppyy.include('FastNoiseLite.h' )
cppyy.include('fastnoise_generator.cpp')