import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class HabiticaApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Habitica App")
        self.setGeometry(100, 100, 800, 600)

        # Crie um objeto QWebEngineView para incorporar o navegador
        self.browser = QWebEngineView(self)

        # Crie um objeto QUrl com a URL que deseja carregar
        url = QUrl("https://habitica.com")

        # Carregue o site Habitica usando o objeto QUrl
        self.browser.setUrl(url)

        # Crie um layout de grade para tornar a janela responsiva
        layout = QGridLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        layout.addWidget(self.browser, 0, 0, 1, 1)

        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HabiticaApp()
    window.show()
    sys.exit(app.exec_())

