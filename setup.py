from distutils.core import setup, Extension

module1 = Extension('matr_utils',
                    sources = ['matr_utils.c', 'algo.c'])

module2 = Extension('numpy_utils',
                    sources = ['numpy_utils.c'],
                    include_dirs = ['/usr/lib/python2.6/site-packages/numpy/core/include'])

setup (name = 'matr_utils',
           version = '1.0',
           description = 'This is a demo package',
           ext_modules = [module1, module2])
