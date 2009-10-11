from distutils.core import setup, Extension

module1 = Extension('matr_utils',
                    sources = ['matr_utils.c', 'algo.c'])

setup (name = 'matr_utils',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
