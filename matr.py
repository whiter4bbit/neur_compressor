from copy import deepcopy
from math import sqrt

def m_debug(X):
    str_ = ""
    for l in X:  str_+="%s\n" % str(l)
    return str_

def flat_square(m, i, j, h, w):
    part = []
    for sub in [a for a in m[i:i+h] ]:
        part.extend(sub[j:j+w])
    subp = [[p[k] for p in part] for k in xrange(3)]
    return subp

def splitt(m, h, w):
    parts = []
    for i in xrange(0, len(m), h):
        for j in xrange(0, len(m[0]), w):
            diff_i, diff_j = i, j
            if i+h>len(m) or j+w>len(m[0]):
                if i+h>len(m): diff_i = len(m)-h
                if j+j>len(m[0]): diff_j = len(m[0])-w
            parts.extend(flat_square(m, diff_i, diff_j, h, w))
    return parts

from random import random as rand

img = [ [(rand(), rand(), rand()) for i in xrange(140)] for j in xrange(160)]

sp = splitt(img, 8,8)

def glue(parts, h, w, m, n):
    glued = [[None for i in xrange(w)] for j in xrange(h)]
    current = 0
    for i in xrange(0, h, m):
        for j in xrange(0, w, n):
            cnt = 0
            diff_i, diff_j = i,j
            if i+m>h: diff_i = h-m
            if j+n>w: diff_j = w-n
            for k in xrange(diff_i,diff_i+m):
                for l in xrange(diff_j,diff_j+n):
                    glued[k][l] = parts[current][cnt]
                    cnt+=1
            current+=1
    return glued

def gluet(parts, h, w, m, n):
    parts_ = []
    for i in xrange(0, len(parts), 3):
        parts_.append([( int(parts[i][k]), int(parts[i+1][k]), int(parts[i+2][k])) for k in xrange(len(parts[i]))])
    return glue(parts_, h, w, m, n)

def norm(m):
    d = deepcopy(m)
    for i in xrange(len(m)):
        for j in xrange(len(m[0])):
            s = sqrt(sum(v[j]*v[j] for v in m))
            d[i][j] = d[i][j]/float(s)
    return d

def transf(m):
    n = deepcopy(m)
    for i in xrange(len(m)):
        for j in xrange(len(m[0])):
            n[i][j] = (2*m[i][j]/255.) - 1
    return n

def detransf(m):
    d = deepcopy(m)
    for i in xrange(len(m)):
        for j in xrange(len(m[0])):
            d[i][j] = 255*(m[i][j]+1)/2
    return d

def centr(m):
    for i in xrange(len(m)):
        for j in xrange(len(m [0])):
            nu = sum(m[k][j] for k in xrange(len(m))) / len(m[0])
            m[i][j] -= nu
    return m

def transp(m):
    t = [[0 for n in xrange(len(m))] for n in xrange(len(m[0]))]
    for i in xrange(len(m)):
        for j in xrange(len(m[0])):
            t[j][i] = m[i][j]
    return t

def minus(a,b):
    c = [ [0 for i in xrange(len(a[0]))] for j in xrange(len(a))]
    for i in xrange(len(a)):
        for j in xrange(len(a[0])):
            c[i][j] = a[i][j]-b[i][j]
    return c

def mult_const(a, const):
    c = [[0 for i in xrange(len(a[0]))] for j in xrange(len(a))]
    for i in xrange(len(a)):
        for j in xrange(len(a[0])):
            c[i][j] = a[i][j]*const
    return c

def mult(a,b):
    return numpy.dot(a,b).tolist()

import numpy

from matr_utils import normalize

class Matrix(object):
    __doc__ = """
    class contains operations for
    working with matrices:
                -- multiply
                -- minus
                -- scale
    """
    __author__="whiter4bbit"
    def __init__(self, m):
        self.m = numpy.array(m)
    def norm(self):
        return Matrix(normalize(self.m.tolist()))
    def scale(self, const):
        return Matrix(self.m*const)
    def dbg():
        return m_debug(self.m)
    def T(self):
        return Matrix(self.m.transpose())
    def __sub__(self, other, context=None):
        return Matrix(self.m- other.m)
    def __mul__(self, other, context=None):
        return Matrix(numpy.dot(self.m, other.m))
    def __repr__(self):
        return m_debug(self.m)
    def __str__(self):
        return m_debug(self.m)

