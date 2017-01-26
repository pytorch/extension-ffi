#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

import my_package.build

this_file = os.path.dirname(__file__)

setup(
    name="my_package",
    version="0.1",
    description="An example project using PyTorch FFI",
    url="https://github.com/pytorch/ffi-examples",
    author="XYZ",
    author_email="author@email.com",
    # Require cffi.
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0"],
    # Exclude the build files.
    packages=find_packages(exclude=["my_package.build"]),
    # Package where to put the extensions. Has to be a prefix of build.py.
    ext_package="my_package",
    # Extensions to compile.
    cffi_modules=[
        os.path.join(this_file, "my_package/build.py:ffi")
    ],
)
