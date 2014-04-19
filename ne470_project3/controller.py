import gui
import Project3Code as p3
from PyQt4 import QtGui


class Controller():
    def __init__(self):
        
        
        dfn = '_currentcore'
        mw,cw = gui.setupMainWindow(self,dfn)
        self.mainwindow = mw
        self.corewidget = cw
        self.mainwindow.show()
        
    def solveStuff(self):
        m,n,w,h,g = self.getParametersFromGui()
        p3.solve(m,n,w,h,g,'_currentcore')
#     def checkCalcFlag(self):
#         if self.corewidget.calcFlag:
#             print('checkCalcFlag')
#             m,n,w,h,g = self.getParametersFromGui()
#             p3.solve(m,n,w,h,g)
#             self.corewidget.calcflag = False
#         
        
    def getParametersFromGui(self):
        w = self.corewidget.xsize
        h = self.corewidget.ysize
        m = self.corewidget.m
        n = self.corewidget.n
        g = self.corewidget.g
        print('Parameters = ',m,n,w,h,g)
        return m,n,w,h,g

if __name__=='__main__':
    app = QtGui.QApplication([])
    
    cntrl = Controller()
        
    app.exec_()
    
    