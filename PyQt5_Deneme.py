from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon, QFont


class DestekMesaj(QWidget):
    def __init__(self, parent=None):
        super(DestekMesaj, self).__init__(parent)

        self.sorunLabel = QLabel("SORUN: ")
        self.sorunLine = QLineEdit()

        destekIzgara = QGridLayout
        destekIzgara.addWidget(self.sorunLabel,0,0)
        destekIzgara.addWidget(self.sorunLine,0,1)

        self.setLayout(destekIzgara)
        self.setWindowTitle("DESTEK")

        #self.kaydetButon = QPushButton("GÖNDER")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    pencere = QWidget()
    pencere.setWindowTitle("DENEME")
    pencere.setFixedSize(640, 480)
    pencere.move(750, 100)
    pencere.setStyleSheet("background-color :lightblue")
    pencere.setWindowIcon(QIcon("1328702.png"))
    yeniPencere = QWidget()

    font1 = QFont()
    font1.setPointSize(14)
    font1.setFamily("Courier New")

    label1 = QLabel("DENEME BAŞARILI MI ?", pencere)
    label1.move(230, 130)
    label1.setFont(font1)

    butonEvet = QPushButton("EVET", pencere)
    butonEvet.move(250, 170)
    butonEvet.setStyleSheet("background-color : white")
    butonHayir = QPushButton("HAYIR", pencere)
    butonHayir.move(350, 170)
    butonHayir.setStyleSheet("background-color : white")


    def showMessageBox():
        QMessageBox.information(yeniPencere, " ", "TAMAM!")
        pencere.destroy()
        app.quit()


    def butonHayirFonksiyonu():
        destekMesaj = DestekMesaj()
        destekMesaj.show()
        pass


    butonEvet.clicked.connect(showMessageBox)
    butonHayir.clicked.connect(butonHayirFonksiyonu)

    pencere.show()
    app.exec_()
