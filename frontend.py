from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui import main
from ui.main import Ui_MainWindow
from img_compressor import ImageCompressor

import Image

class CompressThread(QThread):
    def __init__(self, parent, params, handler):
        QThread.__init__(self, parent)
        self.img = params['img']
        self.m = params['m']
        self.n = params['n']
        self.p = params['p']
        self.params = params

    def handler(self, teach_info):
        self.emit(SIGNAL("handle"), teach_info)

    def debug(self, msg):
        self.emit(SIGNAL("debug"), msg)

    def run(self):
        img = Image.open(self.img)
        self.compr = ImageCompressor(img, self.n, self.m, self.p)
        self.compr.handlers = [self.handler]
        compr = self.compr.compress(self.params)
        self.emit(SIGNAL('compressed'), compr)

class MainWnd(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_app()

    def init_app(self):
        self.src_image = None
        self.reset()
        self.connect(self.ui.actionOpen, SIGNAL("triggered()"), self.load_img)
        self.connect(self.ui.teachButton, SIGNAL("clicked()"), self.teach)
        self.connect(self.ui.mEdit, SIGNAL("textChanged(QString)"), self.rebuildP)
        self.connect(self.ui.nEdit, SIGNAL("textChanged(QString)"), self.rebuildP)

        self.connect(self.ui.pEdit, SIGNAL("textChanged(QString)"), self.rebuildZ)
        self.ui.mEdit.setText('5')
        self.ui.nEdit.setText('5')

    def rebuildP(self, val):
        n,m = self.ui.nEdit.text(), self.ui.nEdit.text()
        if len(n)>0 and len(m)>0:
            p = int(n)*2
            self.ui.pEdit.setText(str(p))
        self.rebuildZ(val)

    def rebuildZ(self, val):
        if str(self.ui.nEdit.text())!='':
            n = int(self.ui.nEdit.text())
        else:
            n = 0
        if str(self.ui.mEdit.text())!='':
            m = int(self.ui.mEdit.text())
        else:
            m = 0
        if str(self.ui.pEdit.text())!='':
            p = int(self.ui.pEdit.text())
        else:
            p = 0
        if self.src_image is not None:
            w,h = self.src_image.rect().width(), self.src_image.rect().height()
            N, L = n*m, (w*h/n*m)*3

            Z = ((N+L)*p+2)/float(N*L)
            self.ui.comprLevelEdit.setText("%2.4f" % Z)

    def reset(self):
        self.ui.debugEdit.setText('')
        self.ui.teachW1ProgressBar.setValue(0)
        self.ui.teachW2ProgressBar.setValue(0)

    def teach(self):
        self.reset()
        self.teach_process()

    def teach_handler(self, teach_info):
        layer = 1
        if layer==0:
            self.ui.teachW1ProgressBar.setMaximum(teach_info['max_iters'])
            self.ui.teachW1ProgressBar.setValue(teach_info['iter'])
        elif layer==1:
            self.ui.teachW2ProgressBar.setMaximum(teach_info['max_iters'])
            self.ui.teachW2ProgressBar.setValue(teach_info['iter'])
        self.debug("Error: %2.5f Alpha: %2.5f, Alpha': %2.5f" % (teach_info['error'], teach_info['alpha'], teach_info['alpha_']))

    def compr_handler(self, img):
        img.save('out.png')
        self.dest_label = QLabel()
        self.dest_image = QImage('out.png')
        to_size = self.ui.comprScrollArea.size()
        self.dest_image = self.dest_image.scaled(to_size, Qt.KeepAspectRatio)
        self.dest_label.setPixmap(QPixmap.fromImage(self.dest_image))
        self.ui.comprScrollArea.setWidget(self.dest_label)

    def debug(self, msg):
        self.ui.debugEdit.setText(self.ui.debugEdit.toHtml()+msg)

    def teach_process(self):
        n = int(self.ui.nEdit.text())
        m = int(self.ui.mEdit.text())
        p = int(self.ui.pEdit.text())

        max_iters =  int(self.ui.maxIterationsSB.value())

        params = {'n':n, 'm':m, 'p':p, 'alpha':.01, 'alpha_':.01, 'out':'compressed.png',\
'img':str(self.srcFileName), 'iters':max_iters}

        if self.ui.adaptiveW1checkBox.checkState()==Qt.Checked:
            params['alpha'] =-1
        if self.ui.adaptiveW2checkBox.checkState()==Qt.Checked:
            params['alpha_']=-1
        thread = CompressThread(self, params, self.teach_handler)
        self.connect(thread, SIGNAL("handle"), self.teach_handler)
        self.connect(thread, SIGNAL("compressed"), self.compr_handler)
        self.connect(thread, SIGNAL("debug"), self.debug)
        thread.start()

    def load_img(self):
        self.srcFileName = \
            QFileDialog.getOpenFileName(self, self.tr("Open image"), QDir.currentPath())

        if self.srcFileName is not None:
            self.src_label = QLabel()
            self.src_image = QImage(self.srcFileName)
            to_size = self.ui.srcScrollArea.size()
            self.src_image = self.src_image.scaled(to_size, Qt.KeepAspectRatio)
            self.src_label.setPixmap(QPixmap.fromImage(self.src_image))
            self.ui.srcScrollArea.setWidget(self.src_label)

import sys

if __name__=="__main__":
    app = QApplication(sys.argv)
    main = MainWnd()
    main.show()
    sys.exit(app.exec_())
