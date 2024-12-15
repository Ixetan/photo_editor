from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap

app = QApplication([])
layout = QVBoxLayout()

buttons_layuot = QHBoxLayout()
open_button = QPushButton("Открыть")
buttons_layuot.addWidget(open_button)
layout.addLayout(buttons_layuot)

buttons_layuot = QHBoxLayout()
next_button = QPushButton("Следуюший")
buttons_layuot.addWidget(next_button)
layout.addLayout(buttons_layuot)

window = QWidget()
window.setLayout(layout)
window.show()

def openFileButtonHandler():
    filename = QFileDialog.getOpenFileName()[0]
    picture = QLabel()
    pixmap = QPixmap(filename).scaledToWidth(1000)
    picture.setPixmap(pixmap)
    layout.addWidget(picture)

def nextFileButtonHandler():
    ...
    

open_button.clicked.connect(openFileButtonHandler)
next_button.clicked.connect(nextFileButtonHandler)


app.exec()