import sys
import pathlib
from PyQt5 import QtWidgets
from UI.addUsers import Ui_AddUsersWidget
from UI.zastava import Ui_Zastava


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Zastava = QtWidgets.QMainWindow()
    AddUsersWidget = QtWidgets.QWidget()
    ui = Ui_Zastava()
    ui2 = Ui_AddUsersWidget()
    ui.setupUi(Zastava)
    # ui.run_yamnet()
    ui2.setupUi(AddUsersWidget)
    Zastava.show()
    sys.exit(app.exec_())