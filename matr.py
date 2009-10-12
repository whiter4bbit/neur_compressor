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

def splitt_(m, h, w):
    parts, i, j = [], 0, 0
    for i in xrange(0,len(m),h):
        for j in xrange(0,len(m[0]),w):
            if i+h<=len(m) and j+w<=len(m[0]):
                p = []
                for a in m[i:i+h]: p.extend(a[j:j+w])
                subp = [[x[k] for x in p] for k in xrange(3)]
                parts.extend(subp)
            else:
                p = []
                i_s, j_s = i,j
                if i+h>len(m): i_s = i-h+1
                if j+w>len(m[0]): j_s =j-w+1

                for a in m[i_s:i_s+h]: p.extend(a[j_s:j_s+w])
                subp = [[x[k] for x in p] for k in xrange(3)]
                parts.extend(subp)
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

def gluet_(parts, h, w, m, n):
    parts_ = []
    for i in xrange(0, len(parts), 3):
        parts_.append([( int(parts[i][k]), int(parts[i+1][k]), int(parts[i+2][k])) for k in xrange(len(parts[i]))])
    glued = [[None for i in xrange(w) ] for j in xrange(h)]
    current = 0
    diffed = 0
    for i in xrange(0, h, m):
        for j in xrange(0, w, n):
            cnt = 0
            for k in xrange(m):
                for l in xrange(n):
                    if (i+m<h and j+n<w):
                        glued[i+k][j+l] = parts_[current][cnt]
                    else:
                        diffed+=1
                        diff_i = i
                        diff_j =j
                        if(i+m>h): diff_i = i+m-h
                        if(j+n>w): diff_j = j+n-w
                        if glued[i+k-diff_i][j+l-diff_j] is None:
                            glued[i+k-diff_i][j+l-diff_j] = parts_[current][cnt]
                    cnt+=1
            current+=1
    print "diff: %d" % diffed
    return glued

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
        self.m = m
    def norm(self):
#        return Matrix(norm(self.m))
        return Matrix(normalize(self.m))
    def scale(self, const):
        return Matrix((numpy.array(self.m)*const).tolist())
#        return Matrix(mult_const(self.m, const))
    def dbg():
        return m_debug(self.m)
    def T(self):
        return Matrix(numpy.array(self.m).transpose().tolist())
    def __sub__(self, other, context=None):
        return Matrix((numpy.array(self.m)- numpy.array(other.m)).tolist())
    def __mul__(self, other, context=None):
        return Matrix(mult(self.m, other.m))
    def __repr__(self):
        return m_debug(self.m)
    def __str__(self):
        return m_debug(self.m)

