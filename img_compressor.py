import Image

from struct import CompressNetw
from matr import gluet, m_debug

class ImageCompressor(object):
    def __init__(self, img, n, m):
        self.img = img
        self.n = n
        self.m = m

    def load(self):
        w,h = self.img.size
        img_rgb = [[0 for i in xrange(w)] for j in xrange(h)]
        print len(img_rgb)
        print len(img_rgb[0])
        for i in xrange(h):
            for j in xrange(w):
                img_rgb[i][j] = self.img.getpixel((j,i))[:3]
        return img_rgb

    def build_netw(self):
        rgbm = self.load()
        compr = CompressNetw(self.n,self.m,self.n*2, rgbm)
        return compr

    def compress(self, out):
        w,h = self.img.size
        netw = self.build_netw()
        parts_ = netw.teach(20)[2]

        compr = gluet(parts_, h, w, self.n*2, self.m)

        img = Image.new("RGBA", (w,h))
        img.save(out)
        for i in xrange(h):
            for j in xrange(w):
                img.putpixel( (j,i) , compr[i][j])
        img.save(out)

import sys

print sys.argv

img = Image.open(sys.argv[1])
imgcompr = ImageCompressor(img,int(sys.argv[2]),int(sys.argv[3]))
imgcompr.compress('compressed.png')

