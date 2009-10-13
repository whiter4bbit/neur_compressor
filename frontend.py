from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui import main
from ui.main import Ui_MainWindow
from img_compressor import ImageCompressor

import Image

class CompressThread(QThread):
    def __init__(self, parent, img, handler):
        QThread.__init__(self, parent)
        self.img = img

    def handler(self, iter, max_iters, layer):
        self.emit(SIGNAL("handle"), iter, max_iters, layer)

    def run(self):
        img = Image.open(self.img)
        self.compr = ImageCompressor(img, 5, 5)
        self.compr.handlers = [self.handler]
        compr = self.compr.compress('compressed.png')
        self.emit(SIGNAL('compressed'), compr)

class MainWnd(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_app()

    def init_app(self):
        self.connect(self.ui.actionOpen, SIGNAL("triggered()"), self.load_img)
        self.connect(self.ui.teachButton, SIGNAL("clicked()"), self.teach)
        self.reset()

    def reset(self):
        self.ui.teachW1ProgressBar.setValue(0)
        self.ui.teachW2ProgressBar.setValue(0)

    def teach(self):
        self.reset()
        self.teach_process()

    def teach_handler(self, iter, max_iters, layer):
        if layer==0:
            self.ui.teachW1ProgressBar.setMaximum(max_iters)
            self.ui.teachW1ProgressBar.setValue(iter)
        elif layer==1:
            self.ui.teachW2ProgressBar.setMaximum(max_iters)
            self.ui.teachW2ProgressBar.setValue(iter)
        print iter, max_iters, layer

    def compr_handler(self, img):
        img.save('out.png')
        self.dest_label = QLabel()
        self.dest_image = QImage('out.png')
        to_size = self.ui.comprScrollArea.size()
        self.dest_image = self.dest_image.scaled(to_size, Qt.KeepAspectRatio)
        self.dest_label.setPixmap(QPixmap.fromImage(self.dest_image))
        self.ui.comprScrollArea.setWidget(self.dest_label)

    def teach_process(self):
        thread = CompressThread(self, str(self.srcFileName), self.teach_handler)
        self.connect(thread, SIGNAL("handle"), self.teach_handler)
        self.connect(thread, SIGNAL("compressed"), self.compr_handler)
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
