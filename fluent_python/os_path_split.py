#!/usr/bin/env python

import os

fullpath = "/home/blake/path/to/nowhere/whereami.jpg"

dirpath, filename = os.path.split(fullpath)

print("dirpath", dirpath)
print("filename", filename)
