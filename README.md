# Introduction

While Python is a coding language that is very easy to write, it comes with some of its own drawbacks, mainly when it comes to efficiency in the code.  One way to improve upon this is to implement functions written in more efficient languages such as C or C++.  This is best for functions that are called often and need to be faster.  One common example is game engines.  It also allows you to use C or C++ libraries in your code.  

# Background information

One of the main ways to import a C/C++ extension is to create a setup.py script that uses setuptools, which is a Python  extension.  This script will work to compile the C/C++ code.  The setup.py can be found in extension-ffi/package.  Then as seen in the extension-ffi/package/script/src folder there are C++ files.  These files are parts of the code that can be more efficiently written in other languages and Python can import.  From here we can do a forward pass, and pass it into C/C++.  This is just a calculation process of the output layers based on the input parameters.  Then a backward function gets these output gradients and computes the input using scalar values.  Laslly, you bind the new code to Python in order to be able to use it for your project.  

# PyTorch C FFI examples

In this repository you can find examples showing how to extend PyTorch with
custom C code. To use the ffi you need to install the `cffi` package from pip.

Currently there are two examples:
* `package` - a pip distributable package
* `script` - compiles the code into a local module, that can be later imported
    from other files

You may also want to look at [pytorch/audio](https://github.com/pytorch/audio/)
for an example of a type-generic C FFI extension.
