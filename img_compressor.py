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
        assert params['e_max']

        w,h = self.img.size
        self.netw.iter_handlers = self.handlers
        trained = self.netw.teach(params['e_max'],params['alpha_'], params['alpha'], params['iters'])
        parts_ = trained[2]
        iterations = trained[1]
        compr = gluet(parts_, h, w, self.n, self.m)
        img = Image.new("RGBA", (w,h))
        img.save(params['out'])
        for i in xrange(h):
            for j in xrange(w):
                img.putpixel( (j,i) , compr[i][j])
        pars = {'img':img, 'iters':iterations}
        return pars
        #img.save(out)

def e_iters_graph():
    o = open('a_iters.dat','w')
    for e in [.008, .009, .01, .011, .012, .02, .03, .04]:
            img = Image.open('pics/dog_test.jpg')
            imgcompr = ImageCompressor(img, 5,5,15)
            pars = imgcompr.compress({'out': 'compressed.png', 'alpha_': e, 'alpha':e, 'iters':150, 'e_max':.05})
            print "ITERS: %2.4f %d" % (e, pars['iters'])
            o.write("%2.2f %d\n" % (e, pars['iters']))
    o.close()

import sys

if __name__=="__main__":
    e_iters_graph()
#    print sys.argv

#    img = Image.open(sys.argv[1])
#    imgcompr = ImageCompressor(img,int(sys.argv[2]),int(sys.argv[3]), int(sys.argv[4]))
#    e_max = .02
#    if len(sys.argv)>5:
#        e_max = float(sys.argv[5])
#        print "using error %2.4f" % e_max
#    pars = imgcompr.compress({'out': 'compressed.png', 'alpha_': -1, 'alpha':-1, 'iters':400, 'e_max':e_max})

