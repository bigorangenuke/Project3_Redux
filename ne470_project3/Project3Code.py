
'''
Hunter Ratliff
NE 470 Project 3 (Honors)
Created on Apr 18, 2014

@author: Hunter
'''
# Import the libraries that will be needed.
import math
import numpy as nm
import time
import matplotlib.pyplot as plt


from mpl_toolkits.axes_grid1 import ImageGrid
import core_loader 

def solve(M=10,N=10,W=100,H=100,G=4,filename=None):
    start = time.time()
    
    # User Defined Parameters
    # If you wish to change anything in this problem, the variables that
    # can be modified are located here.
    
    fn = 'smile.core'
    
    LayoutSQ = core_loader.loadCore(fn)
    N = LayoutSQ.shape[1]
    
    
    
    # LayoutSQ=nm.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) # Number of nodes in x direction
    M = N # Number of nodes in y direction
    
    # Calculated Parameters
    dx = W/(N-1) # delta x
    dy = H/(M-1) # delta y
    x = G*(N-2)*(M-2) # number of interior flux points
    x_total = G*N*M # total number of flux points
    
    # Initialize A, B, flux, and source arrays and k
    A = nm.zeros((int(x),int(x)))
    B = nm.zeros((int(x),int(x)))
    flux = nm.ones((int(x),1)) # initial guess for flux
    S = nm.zeros((int(x),1))
    keff = 1 # initial guess for k_eff
    
    # -----------------------------------------------------------------------------
    # Create a materials layout in the slab/core
    # 0 = Water, 1 = PWR fuel, 2 = MOX, 3 = 10 w/o U-235
    
    '''
    # For a N x M General Layout
    # Creates a layout where outer edge nodes are material 0 (water)
    # and all remaining interior nodes are material 1 (fuel)
    # N and M must be greater than or equal to 5 for this layout.
    LayoutSQ = nm.zeros((N,M))
    LayoutSQ[1:int(N-1),1:int(M-1)] = nm.ones((int(N-2),int(M-2)))
    '''
    '''
    # Creates a layout where outer two edge nodes are material 0 (water)
    # and all remaining interior nodes are material 1 (fuel)
    # N and M must be greater than or equal to 5 for this layout.
    LayoutSQ = nm.zeros((N,M))
    LayoutSQ[2:int(N-2),2:int(M-2)] = nm.ones((int(N-4),int(M-4)))
    '''
    
    
    # For a 26 x 26 Checker board Arrangement
    LayoutSQ = core_loader.loadCore(fn)
    # LayoutSQ=nm.array([[1, 1, 1, 1,1,1,1,1,1,1,1,1,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    # LayoutSQ=nm.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    
    
    # Convert the NxM matrix into a (N-2)*(M-2) x 1 vector
    Layout = nm.zeros((int((N-2)*(M-2)),1))
    print(N,M)
    c = 0
    for a in range(0,N-2):
        for b in range(0,M-2):
            Layout[c] = LayoutSQ[int(a+1),int(b+1)]  
            c += 1
    
    # -------------------------------------------------------------------------------
    # Two Group
    if (G==2):
        # Material Properties
        
        # Material 0, Water
        # Group 1 (Fast)
        D0_1 = 1.56203043
        SigmaR0_1 = 0.0237195306
        nuSigmaf0_1 = 0
        # Group 2 (Thermal)
        D0_2 = 0.271615297
        SigmaA0_2 = 0.129136905
        Sigmas0_12 = 0.213397458
        nuSigmaf0_2 = 0
        
        # Material 1, PWR core (fuel)
        # Group 1 (Fast)
        D1_1 = 1.37992144
        SigmaR1_1 = 0.0211759508
        nuSigmaf1_1 = 0.006275169
        # Group 2 (Thermal)
        D1_2 = 0.347982913
        SigmaA1_2 = 0.169504672
        Sigmas1_12 = 0.007792421
        nuSigmaf1_2 = 0.170405298
        
        # Material 2, MOX
        # Group 1 (Fast)
        D2_1 = 1.39077759
        SigmaR2_1 = 0.022618704
        nuSigmaf2_1 = 0.010309801
        # Group 2 (Thermal)
        D2_2 = 0.330231041
        SigmaA2_2 = 0.236973867
        Sigmas2_12 = 0.006917485
        nuSigmaf2_2 = 0.301609993
        
        # Material 3, 10 w/o U-235
        # Group 1 (Fast)
        D3_1 = 1.37295794
        SigmaR3_1 = 0.022231713
        nuSigmaf3_1 = 0.007814325
        # Group 2 (Thermal)
        D3_2 = 0.291040182
        SigmaA3_2 = 0.313600838
        Sigmas3_12 = 0.006906346
        nuSigmaf3_2 = 0.398054212
        
        # Group 1 Variables
        D_1 = [D0_1, D1_1, D2_1, D3_1]
        SigmaR_1 = [SigmaR0_1, SigmaR1_1, SigmaR2_1, SigmaR3_1]
        nuSigmaf_1 = [nuSigmaf0_1, nuSigmaf1_1, nuSigmaf2_1, nuSigmaf3_1]
        
        # Group 2 Variables
        D_2 = [D0_2, D1_2, D2_2, D3_2]
        SigmaA_2 = [SigmaA0_2, SigmaA1_2, SigmaA2_2, SigmaA3_2]
        Sigmas_12 = [Sigmas0_12, Sigmas1_12, Sigmas2_12, Sigmas3_12]
        nuSigmaf_2 = [nuSigmaf0_2, nuSigmaf1_2, nuSigmaf2_2, nuSigmaf3_2]
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Group 1 (of 2) Fast Calculations
        
        for k1 in range(0,int(x/G)):
            # Retrieve indices i,j from k1
            i = int(math.floor((k1)/(N-2)))
            j = k1 - (i*(N-2))    
        
            # Fill the A matrix (Loss)
            matc = int(Layout[k1])
            A[k1,k1] = (2*D_1[matc]/(dx**2)) + (2*D_1[matc]/(dy**2)) + SigmaR_1[matc]
            if (j-1)>=0 and (j-1)<(N-2):
                matl = int(Layout[int(k1-1)])
                A[k1,int(k1-1)] = -D_1[matl]/(dx**2)
            if (j+1)>=0 and (j+1)<(N-2):
                matr = int(Layout[int(k1+1)])
                A[k1,int(k1+1)] = -D_1[matr]/(dx**2)
            if (i+1)>=0 and (i+1)<(M-2):
                matd = int(Layout[int(k1+(N-2))])
                A[k1,int(k1+(N-2))] = -D_1[matd]/(dy**2)
            if (i-1)>=0 and (i-1)<(M-2):
                matu = int(Layout[int(k1-(N-2))])
                A[k1,int(k1-(N-2))] = -D_1[matu]/(dy**2)
            
            # Fill the B matrix (Production)
            B[k1,k1] = nuSigmaf_1[matc]
            B[k1,int(k1+(x/G))] = nuSigmaf_2[matc]
        
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Group 2 (of 2) Thermal Calculations
        
        for k2 in range(int(x/G),int(x)):
            # Retrieve indices i,j from k2
            ok = k2-(x/G) # original k index in format matrix
            i = int(math.floor(ok/(N-2)))
            j = ok - (i*(N-2))    
        
            # Fill the A matrix (Loss)
            matc = int(Layout[int(ok)])
            A[k2,k2] = (2*D_2[matc]/(dx**2)) + (2*D_2[matc]/(dy**2)) + SigmaA_2[matc]
            if (j-1)>=0 and (j-1)<(N-2):
                matl = int(Layout[int(ok-1)])
                A[k2,int(k2-1)] = -D_2[matl]/(dx**2)
            if (j+1)>=0 and (j+1)<(N-2):
                matr = int(Layout[int(ok+1)])
                A[k2,int(k2+1)] = -D_2[matr]/(dx**2)
            if (i+1)>=0 and (i+1)<(M-2):
                matd = int(Layout[int(ok+(N-2))])
                A[k2,int(k2+(N-2))] = -D_2[matd]/(dy**2)
            if (i-1)>=0 and (i-1)<(M-2):
                matu = int(Layout[int(ok-(N-2))])
                A[k2,int(k2-(N-2))] = -D_2[matu]/(dy**2)
            
            # Fill the B matrix (Production)
            B[k2,int(k2-(x/G))] = Sigmas_12[matc]
        print('***********A***********')
        print(A)
        print('***********B***********')
        print(B)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Solve for fluxes and k
        
        S = nm.dot(B,flux)
        Ainv = nm.linalg.inv(A)
        # initialize variables for while condition
        maxfluxdiff = 1
        kold = 0
        
        # Iteratively solve for flux and k_eff
        while ((abs(keff-kold)/keff)>0.001) or (maxfluxdiff>0.001):
            Sold = S
            kold = keff
            fluxold = flux
            flux = nm.dot(Ainv,(Sold/kold))
            S = nm.dot(B,flux)
            keff = kold*nm.sum(S)/nm.sum(Sold)
            fluxdiff = abs((flux-fluxold)/flux)
            maxfluxdiff = fluxdiff.max()
            
        
        # This puts the flux values back into a NxM matrix to display the flux values
        # to the user in the same format the core composition was inputed.
        fluxSQ_1 = nm.zeros((N,M))
        fluxSQ_2 = nm.zeros((N,M))
        r = 0
        for p in range(1,N-1):
            for q in range(1,M-1):
                fluxSQ_1[p,q] = flux[r]
                fluxSQ_2[p,q] = flux[int(r+(x/G))]
                r += 1
    
        end = time.time()
        elapsedtime = end - start
        
        # Print Statements
        print('Core materials layout:')
        print(LayoutSQ)
        print('Flux of Fast group (Group 1):')
        print(fluxSQ_1)
        print('Flux of Thermal group (Group 2):')
        print(fluxSQ_2)
        print('k = ', keff)
        print('Elapsed time = ', elapsedtime, ' seconds')
        
        maxv = nm.max(flux)
    
    
    
    
    
        #Create an 8x4 figuer
        fig = plt.figure(1,(8.,4.))
        #Create an image grid obejct with 1 colorbar
        grid = ImageGrid(fig,111,nrows_ncols=(1,2),axes_pad=0.1,cbar_mode='single')
        
        #Add plots
        g0 = grid[0].imshow(fluxSQ_1,cmap = 'jet')
        grid[0].set_title('Group 1')
    
        #g0.set_title('Group 1')
        grid[1].imshow(fluxSQ_2,cmap = 'jet')
        grid[1].set_title('Group 2')
    
        #Set colorbar scale
        grid.cbar_axes[0].colorbar(g0)
    
    
    
        # fig = plt.figure(figsize=(12, 6.4))
    
        # gs = gridspec.GridSpec(1,3,width_ratios=[3,3,1])
    
    
        # ax1 = plt.subplot(gs[0])
        # plt.title('Group 1')
        # plt.imshow(fluxSQ_1,cmap = 'jet',vmin = 0)
    
        # ax2 = plt.subplot(gs[1])
        # plt.title('Group 2')
        # pc = plt.imshow(fluxSQ_2,cmap = 'Greys')
        # ax3 = plt.subplot(gs[2])
        # ax3.axis('off')
        # plt.colorbar()
    
        # print(fluxSQ_2.shape)
    
    
        #cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
        #cax.get_xaxis().set_visible(False)
        #cax.get_yaxis().set_visible(False)
        #cax.patch.set_alpha(0)
        #cax.set_frame_on(False)
        
        plt.figtext(0.45,0.04,"X location (cm)",fontdict={'fontsize':14})
        plt.figtext(0.06,0.6,"Y location (cm)",fontdict={'fontsize':14},rotation=90)
    
        #plt.colorbar(orientation='vertical', label='Flux')
        #ax = fig.add_subplot(111)
        #ax = plt.subplot(111)
        #ax.axis('off')
        #plt.tight_layout()
        #plt.colorbar(cax = ax2)
        #plt.show()
        
        
        
        
        
        
    # -------------------------------------------------------------------------------
    # Four Group
    # Energy Group 1: 1E5 to 2E7 eV
    # Energy Group 2: 3 to 1E5 eV
    # Energy Group 3: 0.2 to 3 eV
    # Energy Group 4: 1E-5 to 0.2 eV
    # Chi = average value of 0.453*exp(-1.036*x)*sinh(sqrt(2.29*x)) over energy group
    
    if (G==4):
        # Material Properties
        
        # Material 0, Water
        # Group 1 (Fast)
        D0_1 = 2.11396456
        SigmaR0_1 = 0.00277833780
        nuSigmaf0_1 = 0
        Chi0_1 = 0
        # Group 2 (Second Fastest)
        D0_2 = 0.698132455
        SigmaR0_2 = 0.0526742376
        Sigmas0_12 = 0.0680920035
        nuSigmaf0_2 = 0
        Chi0_2 = 0
        # Group 3 (Second Slowest)
        D0_3 = 0.447531730
        SigmaR0_3 = 0.130731463
        Sigmas0_23 = 0.0406839401
        nuSigmaf0_3 = 0
        Chi0_3 = 0
        # Group 4 (Thermal)
        D0_4 = 0.218849629
        SigmaA0_4 = 0.128428429
        Sigmas0_34 = 0.284961909
        nuSigmaf0_4 = 0
        Chi0_4 = 0
        
        # Material 1, PWR core
        # Group 1 (Fast)
        D1_1 = 1.80324864
        SigmaR1_1 = 3.95267457*(10**(-3))
        nuSigmaf1_1 = 0.004454564
        Chi1_1 = 0.986562073
        # Group 2 (Second Fastest)
        D1_2 = 0.701600432
        SigmaR1_2 = 0.0463181511
        Sigmas1_12 = 0.0421423763
        nuSigmaf1_2 = 0.008106725
        Chi1_2 = 0.013437928
        # Group 3 (Second Slowest)
        D1_3 = 0.548306942
        SigmaR1_3 = 0.109454699
        Sigmas1_23 = 0.0251591336
        nuSigmaf1_3 = 0.0582084432
        Chi1_3 = 2.25388*(10**(-9))
        # Group 4 (Thermal)
        D1_4 = 0.285495579
        SigmaA1_4 = 0.190054342
        Sigmas1_34 = 0.170104995
        nuSigmaf1_4 = 0.208757967
        Chi1_4 = 3.94762*(10**(-11))
        
        # Material 2, MOX
        # Group 1 (Fast)
        D2_1 = 1.78613043
        SigmaR2_1 = 0.004327148
        nuSigmaf2_1 = 0.005736163
        Chi2_1 = 0.98773849
        # Group 2 (Second Fastest)
        D2_2 = 0.689941466
        SigmaR2_2 = 0.047607277
        Sigmas2_12 = 0.041571252
        nuSigmaf2_2 = 0.010269732
        Chi2_2 = 0.012261513
        # Group 3 (Second Slowest)
        D2_3 = 0.498315722
        SigmaR2_3 = 0.19748874
        Sigmas2_23 = 0.024665259
        nuSigmaf2_3 = 0.146808103
        Chi2_3 = 2.08472*(10**(-9))
        # Group 4 (Thermal)
        D2_4 = 0.24343425
        SigmaA2_4 = 0.305939913
        Sigmas2_34 = 0.15191336
        nuSigmaf2_4 = 0.398281008
        Chi2_4 = 7.37869*(10**(-11))
        
        # Material 3, 10 w/o U-235
        # Group 1 (Fast)
        D3_1 = 1.80654311
        SigmaR3_1 = 0.004359475
        nuSigmaf3_1 = 0.005448786
        Chi3_1 = 0.986518979
        # Group 2 (Second Fastest)
        D3_2 = 0.696967542
        SigmaR3_2 = 0.050263368
        Sigmas3_12 = 0.041956231
        nuSigmaf3_2 = 0.016303875
        Chi3_2 = 0.013481026
        # Group 3 (Second Slowest)
        D3_3 = 0.528903902
        SigmaR3_3 = 0.138630837
        Sigmas3_23 = 0.023575004
        nuSigmaf3_3 = 0.113088846
        Chi3_3 = 2.26183*(10**(-9))
        # Group 4 (Thermal)
        D3_4 = 0.260474712
        SigmaA3_4 = 0.274183869
        Sigmas3_34 = 0.161325693
        nuSigmaf3_4 = 0.373362422
        Chi3_4 = 3.96154*(10**(-11))
        
        # Group 1 Variables
        D_1 = [D0_1, D1_1, D2_1, D3_1]
        SigmaR_1 = [SigmaR0_1, SigmaR1_1, SigmaR2_1, SigmaR3_1]
        nuSigmaf_1 = [nuSigmaf0_1, nuSigmaf1_1, nuSigmaf2_1, nuSigmaf3_1]
        Chi_1 = [Chi0_1, Chi1_1, Chi2_1, Chi3_1]
        
        # Group 2 Variables
        D_2 = [D0_2, D1_2, D2_2, D3_2]
        SigmaA_2 = [SigmaR0_2, SigmaR1_2, SigmaR2_2, SigmaR3_2]
        Sigmas_12 = [Sigmas0_12, Sigmas1_12, Sigmas2_12, Sigmas3_12]
        nuSigmaf_2 = [nuSigmaf0_2, nuSigmaf1_2, nuSigmaf2_2, nuSigmaf3_2]
        Chi_2 = [Chi0_2, Chi1_2, Chi2_2, Chi3_2]
        
        # Group 3 Variables
        D_3 = [D0_3, D1_3, D2_3, D3_3]
        SigmaR_3 = [SigmaR0_3, SigmaR1_3, SigmaR2_3, SigmaR3_3]
        Sigmas_23 = [Sigmas0_23, Sigmas1_23, Sigmas2_23, Sigmas3_23]
        nuSigmaf_3 = [nuSigmaf0_3, nuSigmaf1_3, nuSigmaf2_3, nuSigmaf3_3]
        Chi_3 = [Chi0_3, Chi1_3, Chi2_3, Chi3_3]
        
        # Group 4 Variables
        D_4 = [D0_4, D1_4, D2_4, D3_4]
        SigmaA_4 = [SigmaA0_4, SigmaA1_4, SigmaA2_4, SigmaA3_4]
        Sigmas_34 = [Sigmas0_34, Sigmas1_34, Sigmas2_34, Sigmas3_34]
        nuSigmaf_4 = [nuSigmaf0_4, nuSigmaf1_4, nuSigmaf2_4, nuSigmaf3_4]
        Chi_4 = [Chi0_4, Chi1_4, Chi2_4, Chi3_4]
        
        # ~~~~~~~~~~~~~~~~~~~~~~~~
        # Group 1 (of 4) Fast Calculations
        
        for k1 in range(0,int(x/G)):
            # Retrieve indices i,j from k1
            i = int(math.floor((k1)/(N-2)))
            j = k1 - (i*(N-2))    
        
            # Fill the A matrix (Loss)
            matc = int(Layout[k1])
            A[k1,k1] = (2*D_1[matc]/(dx**2)) + (2*D_1[matc]/(dy**2)) + SigmaR_1[matc]
            if (j-1)>=0 and (j-1)<(N-2):
                matl = int(Layout[int(k1-1)])
                A[k1,int(k1-1)] = -D_1[matl]/(dx**2)
            if (j+1)>=0 and (j+1)<(N-2):
                matr = int(Layout[int(k1+1)])
                A[k1,int(k1+1)] = -D_1[matr]/(dx**2)
            if (i+1)>=0 and (i+1)<(M-2):
                matd = int(Layout[int(k1+(N-2))])
                A[k1,int(k1+(N-2))] = -D_1[matd]/(dy**2)
            if (i-1)>=0 and (i-1)<(M-2):
                matu = int(Layout[int(k1-(N-2))])
                A[k1,int(k1-(N-2))] = -D_1[matu]/(dy**2)
            
            # Fill the B matrix (Production)
            B[k1,k1] = Chi_1[matc]*nuSigmaf_1[matc]
            B[k1,int(k1+(x/G))] = Chi_1[matc]*nuSigmaf_2[matc]
            B[k1,int(k1+(2*x/G))] = Chi_1[matc]*nuSigmaf_3[matc]
            B[k1,int(k1+(3*x/G))] = Chi_1[matc]*nuSigmaf_4[matc]
        
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Group 2 (of 4) Second Fastest Calculations
        
        for k2 in range(int(x/G),int(2*x/G)):
            # Retrieve indices i,j from k2
            ok = k2-(x/G) # original k index in format matrix
            i = int(math.floor(ok/(N-2)))
            j = ok - (i*(N-2))    
        
            # Fill the A matrix (Loss)
            matc = int(Layout[int(ok)])
            A[k2,k2] = (2*D_2[matc]/(dx**2)) + (2*D_2[matc]/(dy**2)) + SigmaA_2[matc]
            if (j-1)>=0 and (j-1)<(N-2):
                matl = int(Layout[int(ok-1)])
                A[k2,int(k2-1)] = -D_2[matl]/(dx**2)
            if (j+1)>=0 and (j+1)<(N-2):
                matr = int(Layout[int(ok+1)])
                A[k2,int(k2+1)] = -D_2[matr]/(dx**2)
            if (i+1)>=0 and (i+1)<(M-2):
                matd = int(Layout[int(ok+(N-2))])
                A[k2,int(k2+(N-2))] = -D_2[matd]/(dy**2)
            if (i-1)>=0 and (i-1)<(M-2):
                matu = int(Layout[int(ok-(N-2))])
                A[k2,int(k2-(N-2))] = -D_2[matu]/(dy**2)
            
            # Fill the B matrix (Production)
            B[k2,int(k2-(x/G))] = Sigmas_12[matc]
            B[k2,int(k2)] = Chi_2[matc]*nuSigmaf_2[matc]
            B[k2,int(k2+(x/G))] = Chi_2[matc]*nuSigmaf_3[matc]
            B[k2,int(k2+(2*x/G))] = Chi_2[matc]*nuSigmaf_4[matc]
            
            
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Group 3 (of 4) Second Slowest Calculations
        
        for k3 in range(int(2*x/G),int(3*x/G)):
            # Retrieve indices i,j from k3
            ok = k3-(2*x/G) # original k index in format matrix
            i = int(math.floor(ok/(N-2)))
            j = ok - (i*(N-2))    
        
            # Fill the A matrix (Loss)
            matc = int(Layout[int(ok)])
            A[k3,k3] = (2*D_3[matc]/(dx**2)) + (2*D_3[matc]/(dy**2)) + SigmaA_2[matc]
            if (j-1)>=0 and (j-1)<(N-2):
                matl = int(Layout[int(ok-1)])
                A[k3,int(k3-1)] = -D_3[matl]/(dx**2)
            if (j+1)>=0 and (j+1)<(N-2):
                matr = int(Layout[int(ok+1)])
                A[k3,int(k3+1)] = -D_3[matr]/(dx**2)
            if (i+1)>=0 and (i+1)<(M-2):
                matd = int(Layout[int(ok+(N-2))])
                A[k3,int(k3+(N-2))] = -D_3[matd]/(dy**2)
            if (i-1)>=0 and (i-1)<(M-2):
                matu = int(Layout[int(ok-(N-2))])
                A[k3,int(k3-(N-2))] = -D_3[matu]/(dy**2)
            
            # Fill the B matrix (Production)
            B[k3,int(k3-(x/G))] = Sigmas_23[matc]
            B[k3,int(k3)] = Chi_3[matc]*nuSigmaf_3[matc]
            B[k3,int(k3+(x/G))] = Chi_3[matc]*nuSigmaf_3[matc]
            
            
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Group 4 (of 4) Thermal Calculations
        
        for k4 in range(int(3*x/G),int(4*x/G)):
            # Retrieve indices i,j from k4
            ok = k4-(3*x/G) # original k index in format matrix
            i = int(math.floor(ok/(N-2)))
            j = ok - (i*(N-2))    
        
            # Fill the A matrix (Loss)
            matc = int(Layout[int(ok)])
            A[k4,k4] = (2*D_4[matc]/(dx**2)) + (2*D_4[matc]/(dy**2)) + SigmaA_2[matc]
            if (j-1)>=0 and (j-1)<(N-2):
                matl = int(Layout[int(ok-1)])
                A[k4,int(k4-1)] = -D_4[matl]/(dx**2)
            if (j+1)>=0 and (j+1)<(N-2):
                matr = int(Layout[int(ok+1)])
                A[k4,int(k4+1)] = -D_4[matr]/(dx**2)
            if (i+1)>=0 and (i+1)<(M-2):
                matd = int(Layout[int(ok+(N-2))])
                A[k4,int(k4+(N-2))] = -D_4[matd]/(dy**2)
            if (i-1)>=0 and (i-1)<(M-2):
                matu = int(Layout[int(ok-(N-2))])
                A[k4,int(k4-(N-2))] = -D_4[matu]/(dy**2)
            
            # Fill the B matrix (Production)
            B[k4,int(k4-(x/G))] = Sigmas_34[matc]
            
            
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Solve for fluxes and k
        
        S = nm.dot(B,flux)
        Ainv = nm.linalg.inv(A)
        # initialize variables for while condition
        maxfluxdiff = 1
        kold = 0
        
        # Iteratively solve for flux and k_eff
        while ((abs(keff-kold)/keff)>0.001) or (maxfluxdiff>0.001):
            Sold = S
            kold = keff
            fluxold = flux
            flux = nm.dot(Ainv,(Sold/kold))
            S = nm.dot(B,flux)
            keff = kold*nm.sum(S)/nm.sum(Sold)
            fluxdiff = abs((flux-fluxold)/flux)
            maxfluxdiff = fluxdiff.max()
            
        
        # This puts the flux values back into a NxM matrix to display the flux values
        # to the user in the same format the core composition was inputed.
        fluxSQ_1 = nm.zeros((N,M))
        fluxSQ_2 = nm.zeros((N,M))
        fluxSQ_3 = nm.zeros((N,M))
        fluxSQ_4 = nm.zeros((N,M))
        r = 0
        for p in range(1,N-1):
            for q in range(1,M-1):
                fluxSQ_1[p,q] = flux[r]
                fluxSQ_2[p,q] = flux[int(r+(x/G))]
                fluxSQ_3[p,q] = flux[int(r+(2*x/G))]
                fluxSQ_4[p,q] = flux[int(r+(3*x/G))]
                r += 1
    
        end = time.time()
        elapsedtime = end - start
        
        # Print Statements
        print('Core materials layout:')
        print(LayoutSQ)
        print('Flux of Fastest group (Group 1):')
        print(fluxSQ_1)
        print('Flux of Second Fastest group (Group 2):')
        print(fluxSQ_2)
        print('Flux of Second Slowest group (Group 3):')
        print(fluxSQ_3)
        print('Flux of Thermal group (Group 4):')
        print(fluxSQ_4)
        print('k = ', keff)
        print('Elapsed time = ', elapsedtime, ' seconds')
        
        
        maxv = nm.max(flux)
        # fig = plt.figure(figsize=(12, 6.4))
        # ax = fig.add_subplot(1, 4, 1)
        # ax.set_title('Group 1')
        # plt.imshow(fluxSQ_1, vmin=0, vmax=maxv, cmap='jet', extent=[0, W, 0, H], aspect='equal')
        # ax = fig.add_subplot(1, 4, 2)
        # ax.set_title('Group 2')
        # plt.imshow(fluxSQ_2, vmin=0, vmax=maxv, cmap='jet', extent=[0, W, 0, H], aspect='equal')
        # ax = fig.add_subplot(1, 4, 3)
        # ax.set_title('Group 3')
        # plt.imshow(fluxSQ_3, vmin=0, vmax=maxv, cmap='jet', extent=[0, W, 0, H], aspect='equal')
        # ax = fig.add_subplot(1, 4, 4)
        # ax.set_title('Group 4')
        # plt.imshow(fluxSQ_4, vmin=0, vmax=maxv, cmap='jet', extent=[0, W, 0, H], aspect='equal')
        # cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
        # cax.get_xaxis().set_visible(False)
        # cax.get_yaxis().set_visible(False)
        # cax.patch.set_alpha(0)
        # cax.set_frame_on(False)
        # plt.figtext(0.45,0.24,"X location (cm)",fontdict={'fontsize':18})
        # plt.figtext(0.06,0.6,"Y location (cm)",fontdict={'fontsize':18},rotation=90)
        # plt.colorbar(orientation='horizontal', label='Flux')
        # plt.show()
    
        #Create an 8x4 figuer
        fig = plt.figure(1,(12.,12.))
        #Create an image grid obejct with 1 colorbar
        grid = ImageGrid(fig,111,nrows_ncols=(2,2),axes_pad=0.5,cbar_mode = 'single')#,aspect = False)#,cbar_mode='single')
        
        #Add plots
        g0 = grid[0].imshow(fluxSQ_1,cmap = 'jet')
        grid[0].set_title('Group 1')
    
        #g0.set_title('Group 1')
        grid[1].imshow(fluxSQ_2,cmap = 'jet')
        grid[1].set_title('Group 2')
    
        grid[2].imshow(fluxSQ_3,cmap = 'jet')
        grid[2].set_title('Group 3')
    
        grid[3].imshow(fluxSQ_4,cmap='jet')
        grid[3].set_title('Group 4')
        plt.tight_layout()
        #Set colorbar scale
        grid.cbar_axes[0].colorbar(g0)
    return keff    