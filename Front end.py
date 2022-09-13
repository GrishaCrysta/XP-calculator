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

        def firstr():
            if self.ui.dif.currentIndex() == 0 or 2:
                return Calc.Round(1)
            elif self.ui.dif.currentIndex() == 1:
                return Calc.Round(31)
            elif self.ui.dif.currentIndex() == 3:
                return Calc.Round(3)
            elif self.ui.dif.currentIndex() == 4:
                return Calc.Round(6)

        def finalr():
            if self.ui.dif.currentIndex() == 0:
                return Calc.Round(40)
            elif self.ui.dif.currentIndex() == 1 or 2:
                return Calc.Round(60)
            elif self.ui.dif.currentIndex() == 3:
                return Calc.Round(80)
            elif self.ui.dif.currentIndex() == 4:
                return Calc.Round(100)

        def clicked():
            try:
                game = Calc.Game(firstr(), finalr(), 1 + (self.ui.mapdif.currentIndex() / 10))

                self.ui.XP.setText(str(game.xptoandfromround(int(self.ui.FirstR.text()), int(self.ui.FinalR.text()))) + " XP")

            except:
                self.ui.XP.setText("ERROR")

        def difchange():
            if self.ui.dif.currentIndex() == 0 or self.ui.dif.currentIndex() == 2:
                self.ui.FirstR.setMinimum(1)
                self.ui.FinalR.setMinimum(1)
            elif self.ui.dif.currentIndex() == 1:
                self.ui.FirstR.setMinimum(31)
                self.ui.FinalR.setMinimum(31)
                if int(self.ui.FirstR.text()) < 31:
                    self.ui.FirstR.setValue(31)
                if int(self.ui.FinalR.text()) < 31:
                    self.ui.FinalR.setValue(31)
            elif self.ui.dif.currentIndex() == 3:
                self.ui.FirstR.setMinimum(3)
                self.ui.FinalR.setMinimum(3)
                if int(self.ui.FirstR.text()) < 3:
                    self.ui.FirstR.setValue(3)
                if int(self.ui.FinalR.text()) < 3:
                    self.ui.FinalR.setValue(3)
            elif self.ui.dif.currentIndex() == 4:
                self.ui.FirstR.setMinimum(6)
                self.ui.FinalR.setMinimum(6)
                if int(self.ui.FirstR.text()) < 6:
                    self.ui.FirstR.setValue(6)
                if int(self.ui.FinalR.text()) < 6:
                    self.ui.FinalR.setValue(6)

        self.ui.dif.activated.connect(difchange)
        self.ui.calc.clicked.connect(clicked)


app = QtWidgets.QApplication(sys.argv)
application = MyWindow()
application.show()
sys.exit(app.exec())
