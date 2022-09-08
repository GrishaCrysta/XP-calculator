import Back_end as Calc
from PyQt5 import QtWidgets, uic, QtGui
import sys
from PyQt5.QtCore import Qt

app = QtWidgets.QApplication([])
win = uic.loadUi("gui.ui")
win.XP.setFont(
    QtGui.QFont('Times new roman', 24)
)
win.XP.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
win.t1.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
win.t2.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
win.XP.setText("XP")


def clicked():
    try:
        game = Calc.Game(Calc.Round(int(win.FirstR.text())), Calc.Round(int(win.FinalR.text())))
        win.XP.setText(str(game.xpForGame) + " XP")
    except TypeError:
        win.XP.setText("ERROR")


win.Calc.clicked.connect(clicked)

win.show()
sys.exit(app.exec())
