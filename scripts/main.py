
from my_package import module_1
from my_package.my_subpackage import module_2
from my_package.my_subpackage2.module_3 import printer

if __name__ == "__main__":
    module_1.printer()
    module_2.printer()
    printer()