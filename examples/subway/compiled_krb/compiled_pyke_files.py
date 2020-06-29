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
           [1593471008.0099568, 'subway_rules_bc.py'],
         ('', '', 'subway.kfb'):
           [1593466867.664013, 'subway.fbc'],
        },
        compiler_version)

