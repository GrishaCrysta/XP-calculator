import Back_end as Calc
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from gui import Ui_MainWindow
import sys


class MyWindow(QtWidgets.QDialog):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.XP.setFont(
            QtGui.QFont('Times new roman', 24)
        )
        self.ui.XP.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        self.ui.t1.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        self.ui.t2.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        self.ui.XP.setText("XP")

        def clicked():
            try:
                dif = 1 if self.ui.dif1.isChecked() else 1.1 if self.ui.dif2.isChecked() else 1.2 if self.ui.dif3.isChecked() else 1.3 if self.ui.dif4.isChecked() else 'err'
                game = Calc.Game(Calc.Round(int(self.ui.FirstR.text())), Calc.Round(int(self.ui.FinalR.text())), dif)
                self.ui.XP.setText(str(game.xpForGame) + " XP")
            except TypeError:
                self.ui.XP.setText("ERROR")

        self.ui.calc.clicked.connect(clicked)


app = QtWidgets.QApplication(sys.argv)
application = MyWindow()
application.show()
sys.exit(app.exec())
