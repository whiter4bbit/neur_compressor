from matr import transf, detransf, Matrix,splitt, m_debug

from random import random

class NeurLayer(object):
    __author__ = "whiter4bbit"
    def __init__(self,W):
        self.W = W
    def teach(self, layers, X, alpha):
        pass
    def apply(self, X):
        return X*self.W

class ComprLayer(NeurLayer):
    __author__ = "whiter4bbit"
    def __init__(self, W):
        NeurLayer.__init__(self, W)
    def teach(self, layers, X, alpha):
        Y = self.apply(X)
        X_ = layers[1].apply(Y)
#        alpha = 1/float(sum(x*x for x in X_.m[0]))

        dX = X_- X
        W = self.W
        W = W-X.T().scale(alpha)*dX*layers[1].W.T()
        self.W = W.norm()
        return (dX, X_, self.W)

class DecomprLayer(NeurLayer):
    __author__="whiter4bbit"
    def __init__(self, W):
        NeurLayer.__init__(self, W)
    def teach(self, layers, X, alpha):
        Y = layers[0].apply(X)
#        alpha = 1/float(sum(y*y for y in Y.m[0]))

        X_ = self.apply(Y)
        dX = X_- X
        W_ = self.W
        W_ =W_-Y.T().scale(alpha)*dX
        self.W = W_.norm()
        return (dX, X_, self.W)

import sys

class NeurNetw(object):
    __author__="whiter4bbit"
    def __init__(self, N, p):
        self.N = N
        self.p = p
        self.alpha_ = .1
        self.alpha = 1
        self.iter = 0
        self.__init_matr()

    def re_init(self):
        self.__init_matr()

    def __init_matr(self):
        self.W = Matrix([[random() for r in xrange(self.p)] for i in xrange(self.N)]).norm()
        self.W_ = self.W.T()
        self.layers = [ComprLayer(self.W), DecomprLayer(self.W_)]

    def compress(self, X):
        return self.layers[0].apply(X)

    def decompress(self, X):
        return self.layers[1].apply(X)

    def teach_decompr(self, X, alpha):
        return self.layers[1].teach(self.layers, X, alpha)

    def teach_compress(self, X, alpha):
        return self.layers[0].teach(self.layers, X, alpha)

class CompressNetw(NeurNetw):

    def __init__(self, n,m, p, img):
        NeurNetw.__init__(self, n*m, p)
        self.X = [Matrix([x]) for x in transf(splitt(img,n,m))]
#        with open('x.dump','w') as f:
#            for matr in self.X:
#                f.write(m_debug(matr.m))
        self.L = len(self.X)
        self.N = n*m
        self.Z = ((self.N+self.L)*self.p+2)/float(self.N*self.L)
        print "Z:%2.2f" % self.Z
        print "created matrix with %d components" % len(self.X)

    def teach_layer(self, layer, alpha, max_iters):
        iters = 0
        error = 1e308
        while error>.02 and iters<max_iters:
            E = []
            X_ = []
            for i in xrange(len(self.X)):
                t = self.layers[layer].teach(self.layers, self.X[i], alpha)
                dX = t[0]
                E.append(sum(e*e for e in dX.m[0]))
                X_.append(t[1].m[0])
            print "%d/%d" % (iters, max_iters)
            iters+=1
            error = sum(E)
            print error
        return (error, iters,detransf(X_))

    def teach(self, max_iters):
        NeurNetw.re_init(self)
        print "teaching 1st layer:"
        self.teach_layer(1, .01, max_iters)
        print "teaching 2nd layer:"
        return self.teach_layer(0, .01, max_iters*3)
