# GENERATE PYTHON SCRIPT TO WINDOWS EXECUTABLE
import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.png"
)

# SETUP CX FREEZE
setup(
    name = "RelayBox",
    version = "1.0",
    description = "Modern GUI for Python applications",
    author = "tht5hc@bosch.com",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)

# HOW TO BUILD
# Run this file with option build: ./setup.py build