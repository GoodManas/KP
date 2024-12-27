import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QMainWindow

# Ваши импорты для CheckThread и Ui_MainWindow
from compiled.ui_main import Ui_MainWindow
from compiled.ui_Admin import Ui_Dialog
from api.user import login, register

def check_input(funct):
    def wrapper(self):
        for line_edit in self.base_lane_edit:
            if len(line_edit.text()) == 0: 
                return
        return funct(self)
    return wrapper

class Register(QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btn_login.clicked.connect(self.auth)
        self.ui.btn_register.clicked.connect(self.reg)
        self.base_lane_edit = [self.ui.lineEditLog, self.ui.lineEditPass]

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    @check_input
    def auth(self):
        name = self.ui.lineEditLog.text()
        passw = self.ui.lineEditPass.text()
        login(name, passw)
        print('Authorized')
          
    @check_input 
    def reg(self):
        name = self.ui.lineEditLog.text()
        passw = self.ui.lineEditPass.text()
        register(name, passw)
        print(f'User crerated: {name}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Register()
    window.show()   
    sys.exit(app.exec())