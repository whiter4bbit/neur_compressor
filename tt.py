from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Th(QThread):
    def __init__(self):
        QThread.__init__(self)
    def run(self):
        print "hello, from thread!"

import sys
if __name__=="__main__":
    app = QApplication(sys.argv)
    t = Th()
    t.exec_()
    sys.exit(app.exec_())
