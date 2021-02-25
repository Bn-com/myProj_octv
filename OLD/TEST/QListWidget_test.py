from PySide.QtCore import *
from PySide.QtGui import *
import sys
import os
import glob

class ImageFileList(QListWidget):

    def __init__(self,dirpath,parent=None):
        QListWidget.__init__(self,parent)
        self.setDirpath(dirpath)

    def setDirpath(self,dirpath):
        self._dirpath=dirpath
        self._populate()
        
    def supported_image_extensions(self):
        formats=QImageReader().supportedImageFormats()
        return[str(fmt) for fmt in formats]

    def _images(self):
        images=[]

        for ext in self.supported_image_extensions():
            pattern=os.path.join(self._dirpath,'*.%s'%ext)
            images.extend(glob.glob(pattern))

        return images

    def _populate(self):
        self.clear()

        for image in self._images():
            item=QListWidgetItem(self)
            item.setText(image)
            item.setIcon(QIcon(image))

if __name__=='__main__':
    app=QApplication([])
    win=QWidget()
    win.setWindowTitle('Image List')
    win.setMinimumSize(600,400)
    layout=QVBoxLayout()
    win.setLayout(layout)

    lst=ImageFileList(sys.argv[1],win)
    layout.addWidget(lst)

    entry=QLineEdit(win)

    layout.addWidget(entry)

    def on_item_changed(curr,prev):
        entry.setText(curr.text())

    lst.currentItemChanged.connect(on_item_changed)

    win.show()
    app.exec_()