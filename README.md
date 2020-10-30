# Python_package_template
A template for creating new (working) Python packages fast.

# How to use / General idea of the repo
- put all source code (functions, classes, etc) in my_package/
- put all scripts (__main__) to launch experiments in scripts/
- put all tests in my_package/tests/ as my_package/ contains the source code

# How to make it work 
- ```pip install -e .``` in the root directory (where this README is)
- then ```python scripts/main.py```