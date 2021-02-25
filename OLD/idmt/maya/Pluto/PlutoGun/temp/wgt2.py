
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl('F:\my_python_folder\python demo\spinner\content\Spinner.qml'))
web.show()

sys.exit(app.exec_()) 