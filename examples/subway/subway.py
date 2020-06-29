#!/usr/bin/env python3

import sys
import os

# Local version of pyke
PYKE_PATH = "../../pyke-bps"

# Make sure we are working with python3
if not sys.version_info >= (3, 5):
    print("%s needs python 3.5 or later" % __file__)
    sys.exit(-1)

# Make sure we do NOT have pyke installed as a package
# We want to use tve version in BPS and modify it
try:
    import pyke
    print("%s pyke is already installed, uninstall it to use the local version" % __file__)
    sys.exit(-1)
except ModuleNotFoundError:
    pyke_globally_installed = False

if not os.path.isdir(os.path.abspath(PYKE_PATH)):
    print("%s pyke not found in %s or %s" % (__file__, PYKE_PATH, os.path.abspath(PYKE_PATH)))
    sys.exit(-1)

# Add pike to system module location
sys.path.append(PYKE_PATH)


import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal

# Compile and load .krb files in same directory that I'm in (recursively).

def myTest():
    engine = knowledge_engine.engine(__file__)
    engine.activate('subway_rules')
    kb = engine.get_kb('subway')
    kb.dump_universal_facts()
    print("Specific facts are:")
    engine.get_kb('subway').dump_specific_facts()
    # all forward-chaining rules are run
    print("doing proof")
    try:
        stmt = 'subway.at_station(Airport)' # {}
        stmt = 'subway_rules.at_station($a)'
        # take_line($from, $line, $to)
        # stmt = 'subway_rules.take_line(Airport, $a, $b)'
        # stmt = 'subway_rules.connected(Airport, $b)'
        # stmt = 'subway_rules.half_sibling($af, $bf)'
        with engine.prove_goal(stmt) as gen:
            for variable, plan in gen:
                print(variable)
                # print("%s at_station" % (variable['a']))
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    print()
    print("done")
    engine.print_stats()

# fb = fact_base(engine, 'fb_name')
# fb.dump_universal_facts()
# fb.dump_specific_facts()
# fc_test()

myTest()
