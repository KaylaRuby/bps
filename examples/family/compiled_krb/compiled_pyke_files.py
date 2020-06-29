# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'example.krb'):
           [1593470678.602714, 'example_bc.py'],
         ('', '', 'family.kfb'):
           [1593469475.1843824, 'family.fbc'],
        },
        compiler_version)

