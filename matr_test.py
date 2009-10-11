import matr_utils
from matr import m_debug

def dump_list(lst, name):
    with open(name+'.dump', 'w') as f:
        f.write(m_debug(lst))

def test_norm():
    normal = matr_utils.normalize([[1,2,3], [1,2,3]])
    for i in [40,50,100]:
        na = norm_array(i,i)
        if not na[0]:
            dump_list(na[1], 'src')
            python_var = norm(na[1])
            dump_list(python_var, 'python.dump')
            c_var = matr_utils.normalize(na[1])
            dump_list(c_var, 'c.dump')
            compare_arrays(python_var, c_var)
            raise ValueError("assertion fault!")

def compare_arrays(arr1, arr2):
    for i in xrange(len(arr1)):
        for j in xrange(len(arr1[0])):
            if arr1[i][j]!=arr2[i][j]:
                raise ValueError("Elements at (%d,%d)not equals!", (i,j))

from random import random

from matr import norm

def norm_array(n,m):
    m = [[random() for i in xrange(n)] for j in xrange(m)]
    return (norm(m)==matr_utils.normalize(m),m)

if __name__=="__main__":
    for func in dir():
        if func.startswith("test_"):
            print "===%s===" % func
            eval("%s()" % func)

