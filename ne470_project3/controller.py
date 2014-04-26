import gui
import Project3Code as p3
from PyQt4 import QtGui
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
dbg = False
def saveCore(core,filename= None):
    
    #Save the core configuration to a file
    if dbg: print('controller.CoreDockWidget.saveCore()')
    

    
    if not filename:
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save Core to File', filter='*.core')


    f = open(filename,'w')
    for (i,j),nd in np.ndenumerate(core):
        if dbg: (nd)
        nd = int(nd)
        wstr = "%s,%s,%s\n"%(i,j,nd)
        f.write(wstr) 

    if dbg: print(f)
    f.close()

def create_blank_reactor(m,n,material,fn='_kcheck'):
    r = np.empty((m,n))
    r.fill(int(material))
    saveCore(r,fn)

    return fn




def findMinimumCriticalDimension(filename=None,groups=2):
    #This passes m and n, but the solve function figures that out for itself
    m = 49
    n = 49
    g = groups

    x = 10

    sv = []
    k = [0]
    
    fn= None
    if not filename:
        fn = create_blank_reactor(m,n,2)
        #fn = 'tradition_49.core'
        
    else:
        fn = filename
        
        
        
    #Basic search
    #Calculates k at 5 cm increments
    #When k>1, walk backwards in 1 cm increments until k<1
    if g==2:
        #Counting up flag
        goingup = True
        #done flag for while loop
        done = False
        
        while True:
            k,phi1,phi2,s = p3.solve(m,n,x,x,2,fn,False)
            sv.append([x,k[-1]])
            if done: break
            if k[-1]<1:
                if goingup==False:
                    x+=1
                    done = True
                    goingup=True
                else:
                    #step up in 5 cm increments
                    x+=5
            elif k[-1]>1:
                #when k exceeds one, start walking back in 1 cm increments
                x-=1
                goingup = False
            
        return sv
                
    elif g==4:
        goingup = True
        done = False
        while True:
            k,phi1,phi2,phi3,phi4,s = p3.solve(m,n,x,x,4,fn,False)
            sv.append([x,k[-1]])
            if done: break
            #print(x,k[-1])
            if k[-1]<1:
                if goingup==False:
                    x+=1
                    done = True
                    goingup=True
                else:
                    x+=5
            elif k[-1]>1:
                x-=1
                goingup = False
        
        return sv
    else: assert(False)

def projection(m,n,w,h,g,phi1,phi2,phi3=None,phi4=None,axis=0,subplot=111):

    x = np.linspace(0,w,m)
    
    plt.subplot(subplot)
    
    lineweight = 2
    if g==2:   
        phi1p = np.mean(phi1,axis=axis)
        phi2p = np.mean(phi2,axis=axis)

        plt.plot(x,phi1p,label='Fast',lw=lineweight)
        plt.plot(x,phi2p,label='Thermal',lw=lineweight)
     
    elif g==4:
        phi1p = np.mean(phi1,axis=axis)
        phi2p = np.mean(phi2,axis=axis)
        phi3p = np.mean(phi3,axis=axis)
        phi4p = np.mean(phi4,axis=axis)

        plt.plot(x,phi1p,label='Group 1',lw=lineweight)
        plt.plot(x,phi2p,label='Group 2',lw=lineweight)
        plt.plot(x,phi3p,label='Group 3',lw=lineweight)
        plt.plot(x,phi4p,label='Thermal',lw=lineweight)
        
    if axis ==0:
        plt.title('Projection in x')
        plt.xlabel('Distance along x (cm)')
    elif axis ==1:
        plt.title('Projection in y')
        plt.xlabel('Distance along y (cm)')
    elif axis==2: 
        plt.title('what')
    else:
        print('axis not recognized')
        assert(False)
    
    plt.ylabel('Flux')
    plt.legend()




class Controller():
    def __init__(self):
        
        
        dfn = '_currentcore'
        mw,cw = gui.setupMainWindow(self,dfn)
        self.mainwindow = mw
        self.corewidget = cw
        self.mainwindow.show()
        self.k = None
        self.phi1 = None
        self.phi2 = None
        self.phi3 = None
        self.phi4 = None
        
        
    def solveStuff(self):
        m,n,w,h,g = self.getParametersFromGui()
        self.m = m
        self.n = n
        self.w = w
        self.h = h
        self.g = g
        if g==2:
            k,phi1,phi2,s=p3.solve(m,n,w,h,g,'_currentcore')
            self.k = k[-1]
            self.phi1 = phi1
            self.phi2 = phi2
        elif g==4:
            k,phi1,phi2,phi3,phi4,s=p3.solve(m,n,w,h,g,'_currentcore')
            self.k = k[-1]
            self.phi1 = phi1
            self.phi2 = phi2
            self.phi3 = phi3
            self.phi4 = phi4
            
        self.corewidget.kLineEdit.setText(str(self.k))
        
        #Projections
#         if True:
#             fig = plt.figure()
#             self.projection(0,111)
#             plt.savefig()
#             #plt.show()
            
        if False:
            fig=plt.figure()
            print(s[-1])
            plt.imshow(s[-1])
            #plt.show()
        

    def projection(self,axis,subplot=111):
        x = np.linspace(0,self.w,self.m)
        
        plt.subplot(subplot)
        
        lineweight = 2
        if self.g==2:   
            phi1p = np.mean(self.phi1,axis=axis)
            phi2p = np.mean(self.phi2,axis=axis)

            plt.plot(x,phi1p,label='Fast',lw=lineweight)
            plt.plot(x,phi2p,label='Thermal',lw=lineweight)
         
        elif self.g==4:
            phi1p = np.mean(self.phi1,axis=axis)
            phi2p = np.mean(self.phi2,axis=axis)
            phi3p = np.mean(self.phi3,axis=axis)
            phi4p = np.mean(self.phi4,axis=axis)

            plt.plot(x,phi1p,label='Group 1',lw=lineweight)
            plt.plot(x,phi2p,label='Group 2',lw=lineweight)
            plt.plot(x,phi3p,label='Group 3',lw=lineweight)
            plt.plot(x,phi4p,label='Thermal',lw=lineweight)
            
        if axis ==0:
            plt.title('Projection in x')
            plt.xlabel('Distance along x (cm)')
        elif axis ==1:
            plt.title('Projection in y')
            plt.xlabel('Distance along y (cm)')
        elif axis==2: 
            plt.title('what')
        else:
            print('axis not recognized')
            assert(False)
        
        plt.ylabel('Flux')
        plt.legend()
    
        
    def getParametersFromGui(self):
        w = self.corewidget.xsize
        h = self.corewidget.ysize
        m = self.corewidget.m
        n = self.corewidget.n
        g = self.corewidget.g
        print('Parameters = ',m,n,w,h,g)
        return m,n,w,h,g


if __name__=='__main__':
#     gs = [2,4]
# #     
# #     for g in gs:
# #         c = findMinimumCriticalDimension(None,g)
# #         print('Minimum critical dimensions for %s groups: %s'%(g,c[-1]))
#     
#     
# #     files = ['config4_49_10leu_mox.core','config4_49_leu_10leu.core','config4_49_leu_mox.core']
# #     for fn in files:
# #         for g in gs:
# #             c = findMinimumCriticalDimension(fn,g)
# #             print('Minimum critical dimensions for %s groups %s: %s'%(g,fn,c[-1]))
#     files = ['tradition_49.core','tradition_49_mox.core','tradition_49_10leu.core',
#      'config1_49.core','config1_49_10leu_leu.core','config1_49_mox_leu.core',
#      'config4_49_10leu_mox.core','config4_49_leu_10leu.core','config4_49_leu_mox.core']
# 
#     #files = ['ut.core']
#     
# 
#     for g in gs:
# #         c = findMinimumCriticalDimension(file,g)
# #         #rint('Minimum critical dimensions for %s groups %s: %s'%(g,file,c[-1]))
# #         x = c[-1][0]
#         vals = None
#         for file in files:
#             if file=='tradition_49.core': vals = [38,11]
#             elif file=='tradition_49_mox.core': vals = [33,15]
#             elif file=='tradition_49_10leu.core': vals = [32,15]
#             elif file=='config1_49.core': vals = [69,14]
#             elif file=='config1_49_10leu_leu.core': vals = [48,16]
#             elif file=='config1_49_mox_leu.core': vals = [47,16]
#             elif file=='config4_49_10leu_mox.core': vals = [29,16]
#             elif file=='config4_49_leu_10leu.core': vals = [33,13]
#             elif file=='config4_49_leu_mox.core': vals = [33,13]
#             else:
#                 print('file name not recognized')
#                 assert(False)
#                 
#             if g==2:
#                 x=vals[0]
#                 k,phi1,phi2,s=p3.solve(49,49,x,x,g,file,False,True)
#                 
#                 fn = file.split('.')
#                 f = open('%s_%sgroups_dump'%(fn[0],g),'w')
#                 f.write('filename:%s\n'%(file))
#                 f.write('groups:%s\n'%(g))
#                 f.write('m:49\n')
#                 f.write('n:49\n')
#                 f.write('x:%s\n'%(x))
#                 f.write('y:%s\n'%(x))
#                 f.write('k:%s\n'%(k[-1]))
#                 f.write('#phi1:\n')
#                 for (i,j),p in np.ndenumerate(phi1):
#                     f.write('%s,%s,%s\n'%(i,j,p))
#                 f.write('#phi2:\n')
#                 for (i,j),p in np.ndenumerate(phi2):
#                     f.write('%s,%s,%s\n'%(i,j,p))
#                 f.close()
#                 fig = plt.figure()
#                 fig = projection(49,49,x,x,g,phi1,phi2,None,None,0)
#                 plt.savefig('%s_xprojection_%sgroups.png'%(file,g))
#                 fig = plt.figure()
#                 fig = projection(49,49,x,x,g,phi1,phi2,None,None,1)
#                 plt.savefig('%s_yprojection_%sgroups.png'%(file,g))
#                  
#                 fig = plt.figure()
#                 plt.plot(k)
#                 plt.title('Convergence of k')
#                 plt.xlabel('Iteration')
#                 plt.ylabel('$k_{eff}$')
#                 plt.savefig('%s_kconvergence_%sgroups.png'%(file,g))
#             elif g==4:
#                 x=vals[1]
#                 k,phi1,phi2,phi3,phi4,s=p3.solve(49,49,x,x,g,file,False,True)
#                 fn = file.split('.')
#                 f = open('%s_%sgroups_dump'%(fn[0],g),'w')
#                 f.write('filename:%s\n'%(file))
#                 f.write('groups:%s\n'%(g))
#                 f.write('m:49\n')
#                 f.write('n:49\n')
#                 f.write('x:%s\n'%(x))
#                 f.write('y:%s\n'%(x))
#                 f.write('k:%s\n'%(k[-1]))
#                 f.write('#phi1:\n')
#                 for (i,j),p in np.ndenumerate(phi1):
#                     f.write('%s,%s,%s\n'%(i,j,p))
#                 f.write('#phi2:\n')
#                 for (i,j),p in np.ndenumerate(phi2):
#                     f.write('%s,%s,%s\n'%(i,j,p))
#                 f.write('#phi3:\n')
#                 for (i,j),p in np.ndenumerate(phi3):
#                     f.write('%s,%s,%s\n'%(i,j,p))
#                 f.write('#phi4:\n')
#                 for (i,j),p in np.ndenumerate(phi2):
#                     f.write('%s,%s,%s\n'%(i,j,p))
#                 f.close()
# #                  
#                 fig = plt.figure()
#                 fig = projection(60,60,x,x,g,phi1,phi2,phi3,phi4,0)
#                 plt.savefig('%s_xprojection_%sgroups.png'%(file,g))
#                   
#                 fig = plt.figure()
#                 fig = projection(60,60,x,x,g,phi1,phi2,phi3,phi4,1)
#                 plt.savefig('%s_yprojection_%sgroups.png'%(file,g))
#                   
#                 fig = plt.figure()
#                 plt.plot(k)
#                 plt.title('Convergence of k')
#                 plt.xlabel('Iteration')
#                 plt.ylabel('$k_{eff}$')
#                 plt.savefig('%s_kconvergence_%sgroups.png'%(file,g))

     

    app = QtGui.QApplication([])
    
    cntrl = Controller()
    
    app.exec_()
      
    