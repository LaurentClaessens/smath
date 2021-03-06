#! /usr/bin/python3
# -*- coding: utf8 -*-

# The directory passed as argument is the main directory of the
# smath project.
#

# This script only works when the directory of 'phystricks' is in
# $PYTHONPATH
# The reason is that we need to import 'TestRecall'

import sys
import os
import importlib.util

# Get the path in which to find the module 'phystricks'
spec=importlib.util.find_spec('phystricks')
phystricks_dir=spec.submodule_search_locations[0]

# Append to 'sys.path' the name of the directory in which is 'TestRecall.py'
test_recall_file=os.path.join(phystricks_dir,"testing/recall_tests/TestRecall.py")
sys.path.append(os.path.dirname(test_recall_file))

# Import 'TestRecall'
TestRecall = importlib.import_module("TestRecall")

directory=sys.argv[1]

pstricks_directory=directory
recall_directory=directory

TestRecall.check_pictures(pstricks_directory,recall_directory)
