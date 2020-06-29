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
         ('', '', 'subway_rules.krb'):
           [1593465985.008032, 'subway_rules_bc.py'],
         ('', '', 'subway.kfb'):
           [1593465512.647649, 'subway.fbc'],
        },
        compiler_version)

