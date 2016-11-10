import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        self.loadFinished.connect(self._result_available)

    def _result_available(self, ok):
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.load(QUrl("https://maps.google.com"))
    sys.exit(app.exec_())