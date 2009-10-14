import Image

from struct import CompressNetw
from matr import gluet, m_debug

class ImageCompressor(object):
    def __init__(self, img, n, m, p):
        self.img = img
        self.n = n
        self.m = m
        self.p = p
        self.handlers = []
        self.netw = self.build_netw()

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
        compr = CompressNetw(self.n,self.m,self.p, rgbm)
        return compr

    def compress(self, params):
        assert params['alpha_']
        assert params['alpha']
        assert params['out']
        assert params['iters']

        w,h = self.img.size
        self.netw.iter_handlers = self.handlers
        parts_ = self.netw.teach(params['alpha_'], params['alpha'], params['iters'])[2]
        compr = gluet(parts_, h, w, self.n, self.m)
        img = Image.new("RGBA", (w,h))
        img.save(params['out'])
        for i in xrange(h):
            for j in xrange(w):
                img.putpixel( (j,i) , compr[i][j])
        return img
        #img.save(out)

import sys

if __name__=="__main__":
    print sys.argv

    img = Image.open(sys.argv[1])
    imgcompr = ImageCompressor(img,int(sys.argv[2]),int(sys.argv[3]), int(sys.argv[4]))
    imgcompr.compress({'out': 'compressed.png', 'alpha_': .01, 'alpha':.01})
