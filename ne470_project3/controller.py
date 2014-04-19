import gui
import Project3Code as p3
from PyQt4 import QtGui


if __name__=='__main__':
    dfn = 'smile.core'
    
    app = QtGui.QApplication([])
    mainwindow =gui.setupMainWindow(dfn)
    k = p3.solve()
    mainwindow.show()
    app.exec_()
    
    