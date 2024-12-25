from PySide6 import QtCore, QtGui, QtWidgets

from handler.connection import *

class CheckThread(QtCore.QThread):
    mysignal = QtCore.Signal(str)
    
    def thr_login(self, name, passw):
        login(name, passw, self.mysignal)
        
    def thr_register(self, name, passw):
        register(name, passw, self.mysignal)

