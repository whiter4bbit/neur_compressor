def m_debug(X):
    str_ = ""
    for l in X:  str_+="%s\n" % str(l)
    return str_

def flat_square(m, i, j, h, w):
    part = []
    for sub in [a for a in m[i:i+h] ]:
        part.extend(sub[j:j+w])
    return part

def split(m, h, w):
    parts = []
    for i in xrange(0, len(m), h):
        for j in xrange(0, len(m[0]), w):
            diff_i, diff_j = i, j
            if i+h>len(m): diff_i = len(m)-h
            if j+j>len(m[0]): diff_j = len(m[0])-w
            parts.append(flat_square(m, diff_i, diff_j, h, w))
    return parts

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

from random import randint

test = [ [randint(0,100) for i in xrange(14)]  for j in xrange(16)]

test2 = [[1,2,3,4], [4,5,6,7], [9,10,11,12]]

splitted = split(test2, 2, 2)
print m_debug(test2)
print "split:"
print m_debug(splitted)

print "glued:"
print m_debug(glue(splitted, 3, 4, 2, 2))

