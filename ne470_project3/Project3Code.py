
'''
Hunter Ratliff
NE 470 Project 3 (Honors)
Created on Apr 18, 2014

Modified by Joseph Conner

@author: Hunter
'''
# Import the libraries that will be needed.
import math
import numpy as nm
import time
import matplotlib.pyplot as plt


from mpl_toolkits.axes_grid1 import ImageGrid
import core_loader 
dbg = False

def solve(M=10,N=10,W=100,H=100,G=4,filename=None,doPlot = True,doSave=False):
    if dbg: print('Project3Code.solve start')
    start = time.time()
    
    # User Defined Parameters
    # If you wish to change anything in this problem, the variables that
    # can be modified are located here.
    if not filename:
        filename = '_kcheck.core'



    fn = filename
    
    LayoutSQ = core_loader.loadCore(fn)
    N = LayoutSQ.shape[1]
    M = N # Number of nodes in y direction
    
    track_k = []
    track_s = []
    
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
    track_k.append(keff)
    track_s.append(S)
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

    
    # Convert the NxM matrix into a (N-2)*(M-2) x 1 vector
    Layout = nm.zeros((int((N-2)*(M-2)),1))
    if dbg: print(N,M)
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
        sigmaf0_1 = 0
        # Group 2 (Thermal)
        D0_2 = 0.271615297
        SigmaA0_2 = 0.129136905
        Sigmas0_12 = 0.213397458
        nuSigmaf0_2 = 0
        sigmaf0_2 = 0
        
        # Material 1, PWR core (fuel)
        # Group 1 (Fast)
        D1_1 = 1.47514248
        SigmaR1_1 = 8.89804307e-03
        nuSigmaf1_1 = 7.58585753e-03
        sigmaf1_1 = 2.98927375E-03
        # Group 2 (Thermal)
        D1_2 = 3.34128827e-01
        SigmaA1_2 = 9.00137126e-02
        Sigmas1_12 = 1.93917640e-02
        nuSigmaf1_2 = 1.36130318e-01
        sigmaf1_2 = 5.58666699E-02
        
        # Material 2, MOX
        # Group 1 (Fast)
        D2_1 = 1.46842682
        SigmaR2_1 = 1.10678272e-2
        nuSigmaf2_1 = 9.30305105e-3
        sigmaf2_1 = 3.27444798E-03
        # Group 2 (Thermal)
        D2_2 = 2.95294464e-01
        SigmaA2_2 = 1.63709238e-1
        Sigmas2_12 = 1.74693074e-2
        nuSigmaf2_2 = 2.61087507e-1
        sigmaf2_2 = 9.13106427E-02
        
        # Material 3, 10% U-235
        # Group 1 (Fast)
        D3_1 = 1.48997104
        SigmaR3_1 = 1.14417057e-2
        nuSigmaf3_1 = 1.27420006e-2
        sigmaf3_1 = 5.09099523E-03
        # Group 2 (Thermal)
        D3_2 = 3.22502375e-01
        SigmaA3_2 = 1.29340038e-1
        Sigmas3_12 = 1.75550431e-2
        nuSigmaf3_2 = 2.20225289e-1
        sigmaf3_2 = 9.03785005E-02
		
		# Material 4, 4% U-235 with control rods
        # Group 1 (Fast)
        D4_1 = 1.37992144
        SigmaR4_1 = 0.021175951
        nuSigmaf4_1 = 0.006275169
        sigmaf4_1 = 2.44636997E-03
        # Group 2 (Thermal)
        D4_2 = 0.347982913
        SigmaA4_2 = 0.169504672
        Sigmas4_12 = 0.007792421
        nuSigmaf4_2 = 0.170405298
        sigmaf4_2 = 6.99328110E-02
		
        # Material 5, MOX with control rods
        # Group 1 (Fast)
        D5_1 = 1.39077759
        SigmaR5_1 = 0.022618704
        nuSigmaf5_1 = 0.010309801
        sigmaf5_1 = 2.74634222E-03
        # Group 2 (Thermal)
        D5_2 =0.330231041
        SigmaA5_2 = 0.236973867
        Sigmas5_12 = 0.006917485
        nuSigmaf5_2 = 0.301609993
        sigmaf5_2 = 1.39152989E-01
		
		# Material 6, 10% U-235 with control rods
        # Group 1 (Fast)
        D6_1 = 1.37295794
        SigmaR6_1 = 0.022231713
        nuSigmaf6_1 = 0.007814325
        sigmaf6_1 = 4.08774242E-03
        # Group 2 (Thermal)
        D6_2 =0.291040182
        SigmaA6_2 = 0.313600838
        Sigmas6_12 = 0.006906346
        nuSigmaf6_2 = 0.398054212
        sigmaf6_2 = 1.23778038E-01
		
        # Group 1 Variables
        D_1 = [D0_1, D1_1, D2_1, D3_1,D4_1,D5_1,D6_1]
        SigmaR_1 = [SigmaR0_1, SigmaR1_1, SigmaR2_1, SigmaR3_1, SigmaR4_1, SigmaR5_1, SigmaR6_1]
        nuSigmaf_1 = [nuSigmaf0_1, nuSigmaf1_1, nuSigmaf2_1, nuSigmaf3_1, nuSigmaf4_1, nuSigmaf5_1, nuSigmaf6_1]
        sigmaf_1 = [sigmaf0_1,sigmaf1_1,sigmaf2_1,sigmaf3_1,sigmaf4_1,sigmaf5_1,sigmaf6_1]
        # Group 2 Variables
        D_2 = [D0_2, D1_2, D2_2, D3_2,D4_2,D5_2,D6_2]
        SigmaA_2 = [SigmaA0_2, SigmaA1_2, SigmaA2_2, SigmaA3_2, SigmaA4_2, SigmaA5_2, SigmaA6_2]
        Sigmas_12 = [Sigmas0_12, Sigmas1_12, Sigmas2_12, Sigmas3_12, Sigmas4_12, Sigmas5_12, Sigmas6_12]
        nuSigmaf_2 = [nuSigmaf0_2, nuSigmaf1_2, nuSigmaf2_2, nuSigmaf3_2, nuSigmaf4_2, nuSigmaf5_2, nuSigmaf6_2]
        sigmaf_2 = [sigmaf0_2,sigmaf1_2,sigmaf2_2,sigmaf3_2,sigmaf4_2,sigmaf5_2,sigmaf6_2]
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
        if dbg: print('***********A***********')
        if dbg: print(A)
        if dbg: print('***********B***********')
        if dbg: print(B)
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
            track_s.append(S)
            keff = kold*nm.sum(S)/nm.sum(Sold)
            track_k.append(keff)
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
        if dbg: print('Core materials layout:')
        if dbg: print(LayoutSQ)
        if dbg: print('Flux of Fast group (Group 1):')
        if dbg: print(fluxSQ_1)
        if dbg: print('Flux of Thermal group (Group 2):')
        if dbg: print(fluxSQ_2)
        if dbg: print('k = ', keff)
        if dbg: print('Elapsed time = ', elapsedtime, ' seconds')
        
        maxv = nm.max(flux)

            
    
            
        plt.clf()
        #Create an 8x4 figuer
        fig = plt.figure(1,(12.,6.))
        #Create an image grid obejct with 1 colorbar
        grid = ImageGrid(fig,111,nrows_ncols=(1,2),axes_pad=0.1,cbar_mode='single')
        
        #Add plots
        g0 = grid[0].imshow(fluxSQ_1,cmap = 'jet', vmin=0, vmax=maxv, extent=[0, W, 0, H])
        grid[0].set_title('Group 1')
    
        #g0.set_title('Group 1')
        grid[1].imshow(fluxSQ_2,cmap = 'jet', vmin=0, vmax=maxv, extent=[0, W, 0, H])
        grid[1].set_title('Group 2')
        
        #Set colorbar scale
        grid.cbar_axes[0].colorbar(g0)
        plt.suptitle('$k_{eff}$ = %s'%(track_k[-1]),fontsize=16)
        

        if doSave:
            plt.savefig("%s_%sgroups.png"%(fn,2))
        
        
        plt.plot()
        
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
        
#             fig = plt.figure()
#             plt.plot(track_k)
#             plt.xlabel('Iteration')
#             plt.ylabel('k_eff')
#             #plt.show()
        plt.figtext(0.45,0.04,"X location (cm)",fontdict={'fontsize':14})
        plt.figtext(0.06,0.6,"Y location (cm)",fontdict={'fontsize':14},rotation=90)
        fig.canvas.draw()
        #plt.show()
        
        
        return track_k,fluxSQ_1,fluxSQ_2,track_s
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
        sigmaf0_1 = 0
        # Group 2 (Second Fastest)
        D0_2 = 0.698132455
        SigmaR0_2 = 0.0526742376
        Sigmas0_12 = 0.0680920035
        nuSigmaf0_2 = 0
        Chi0_2 = 0
        sigmaf0_2 = 0
        # Group 3 (Second Slowest)
        D0_3 = 0.447531730
        SigmaR0_3 = 0.130731463
        Sigmas0_23 = 0.0406839401
        nuSigmaf0_3 = 0
        Chi0_3 = 0
        sigmaf0_3 = 0
        # Group 4 (Thermal)
        D0_4 = 0.218849629
        SigmaA0_4 = 0.128428429
        Sigmas0_34 = 0.284961909
        nuSigmaf0_4 = 0
        Chi0_4 = 0
        sigmaf0_4 = 0
        
        # Material 1, PWR core
        # Group 1 (Fast)
        D1_1 = 2.06552434
        SigmaR1_1 = 2.51095160e-3
        nuSigmaf1_1 = 4.74275835e-3
        Chi1_1 = 9.86559808e-1
        sigmaf1_1 = 1.71996362E-03
        # Group 2 (Second Fastest)
        D1_2 = 7.71068096e-1
        SigmaR1_2 = 1.62852854e-2
        Sigmas1_12 = 2.77155012e-1
        nuSigmaf1_2 = 9.38869640e-3
        Chi1_2 = 1.34401778e-2
        sigmaf1_2 = 3.85293062E-03
        # Group 3 (Second Slowest)
        D1_3 = 5.91071784e-1
        SigmaR1_3 = 3.70188504e-2
        Sigmas1_23 = 4.65827212e-2
        nuSigmaf1_3 = 5.44131398e-2
        Chi1_3 = 2.25429297e-09
        sigmaf1_3 = 2.23306660E-02
        # Group 4 (Thermal)
        D1_4 = 2.82853842e-1
        SigmaA1_4 = 1.01570554e-1
        Sigmas1_34 = 2.25025505e-1
        nuSigmaf1_4 = 1.53005496-1
        Chi1_4 = 3.94835033e-11
        sigmaf1_4 = 6.27920926E-02
        
        # Material 2, MOX
        # Group 1 (Fast)
        D2_1 = 2.04261065
        SigmaR2_1 = 2.90366588e-3
        nuSigmaf2_1 = 6.06630696e-3
        Chi2_1 = 9.87740934e-1
        sigmaf2_1 = 2.09894124E-03
        # Group 2 (Second Fastest)
        D2_2 = 7.57412732e-1
        SigmaR2_2 = 1.78555362e-2
        Sigmas2_12 = 4.72660773e-2
        nuSigmaf2_2 = 1.19549464e-2
        Chi2_2 = 1.22590568e-2
        sigmaf2_2 = 4.24945541E-03
        # Group 3 (Second Slowest)
        D2_3 = 5.49056292e-1
        SigmaR2_3 = 1.04033530e-1
        Sigmas2_23 = 4.58983518e-2
        nuSigmaf2_3 = 1.32770360e-1
        Chi2_3 = 2.08438955e-9
        sigmaf2_3 = 4.63567451E-02
        # Group 4 (Thermal)
        D2_4 = 2.52859473e-1
        SigmaA2_4 = 1.56617731e-1
        Sigmas2_34 = 2.01856598e-1
        nuSigmaf2_4 = 2.48021170e-1
        Chi2_4 = 7.38793124e-11
        sigmaf2_4 = 8.68968517E-02
        
        # Material 3, 10% U-235
        # Group 1 (Fast)
        D3_1 = 2.06963658
        SigmaR3_1 = 2.92107626e-3
        nuSigmaf3_1 = 5.74169448e-3
        Chi3_1 = 9.86518443e-1
        sigmaf3_1 = 2.10944354E-03
        # Group 2 (Second Fastest)
        D3_2 = 7.63395727e-1
        SigmaR3_2 = 2.11307574e-2
        Sigmas3_12 = 4.77483124e-2
        nuSigmaf3_2 = 1.83885992e-2
        Chi3_2 = 1.34815481e-2
        sigmaf3_2 = 7.54626608E-03
        # Group 3 (Second Slowest)
        D3_3 = 5.76803029e-1
        SigmaR3_3 = 5.90367839e-2
        Sigmas3_23 = 4.43177074e-2
        nuSigmaf3_3 = 9.99740362e-2
        Chi3_3 = 2.26192087e-9
        sigmaf3_3 = 4.10284549E-02
        # Group 4 (Thermal)
        D3_4 = 2.64549017e-1
        SigmaA3_4 = 1.45154640e-1
        Sigmas3_34 = 2.11455747e-1
        nuSigmaf3_4 = 2.45367095e-1
        Chi3_4 = 3.96171013e-11
        sigmaf3_4 = 1.00696474E-01
		
		# Material 4, 4% U-235 with control rods
        # Group 1 (Fast)
        D4_1 = 1.80324864
        SigmaR4_1 = 0.003952675
        nuSigmaf4_1 = 0.004454564
        Chi4_1 = 0.986562073
        sigmaf4_1 = 1.61944935E-03
        # Group 2 (Second Fastest)
        D4_2 = 0.701600432
        SigmaR4_2 = 0.046318151
        Sigmas4_12 = 0.042142376
        nuSigmaf4_2 = 0.008106725
        Chi4_2 = 0.013437928
        sigmaf4_2 = 3.32679390E-03
        # Group 3 (Second Slowest)
        D4_3 = 0.548306942
        SigmaR4_3 = 0.109454699
        Sigmas4_23 = 0.025159134
        nuSigmaf4_3 = 0.058208443
        Chi4_3 = 2.25388e-09
        sigmaf4_3 = 2.38882266E-02
        # Group 4 (Thermal)
        D4_4 = 0.285495579
        SigmaA4_4 = 0.190054342
        Sigmas4_34 = 2.11455747e-1
        nuSigmaf4_4 = 0.208757967
        Chi4_4 = 3.94762e-11
        sigmaf4_4 = 8.56724158E-02
		
        # Material 5, MOX with control rods
        # Group 1 (Fast)
        D5_1 = 1.78613043
        SigmaR5_1 = 0.004327148
        nuSigmaf5_1 = 0.005736163
        Chi5_1 = 0.98773849
        sigmaf5_1 = 1.98864494E-03
        # Group 2 (Second Fastest)
        D5_2 = 0.689941466
        SigmaR5_2 = 0.047607277
        Sigmas5_12 = 0.041571252
        nuSigmaf5_2 = 0.010269732
        Chi5_2 = 0.012261513
        sigmaf5_2 = 3.65130370E-03
        # Group 3 (Second Slowest)
        D5_3 = 0.498315722
        SigmaR5_3 = 0.19748874
        Sigmas5_23 = 0.024665259
        nuSigmaf5_3 = 0.146808103
        Chi5_3 = 2.08472e-09
        sigmaf5_3 = 5.12913205E-02
        # Group 4 (Thermal)
        D5_4 = 0.24343425
        SigmaA5_4 = 0.305939913
        Sigmas5_34 = 0.15191336
        nuSigmaf5_4 = 0.398281008
        Chi5_4 = 7.37869e-11
        sigmaf5_4 = 1.39537483E-01

        # Material 6, 10% U-235 with control rods
        # Group 1 (Fast)
        D6_1 = 1.80654311
        SigmaR6_1 = 0.004359475
        nuSigmaf6_1 = 0.005448786
        Chi6_1 = 0.986518979
        sigmaf6_1 = 2.10944354E-03
        # Group 2 (Second Fastest)
        D6_2 = 0.696967542
        SigmaR6_2 = 0.050263368
        Sigmas6_12 = 0.041956231
        nuSigmaf6_2 = 0.016303875
        Chi6_2 = 0.013481026
        sigmaf6_2 = 7.54626608E-03
        # Group 3 (Second Slowest)
        D6_3 = 0.528903902
        SigmaR6_3 = 0.138630837
        Sigmas6_23 = 0.023575004
        nuSigmaf6_3 = 0.113088846
        Chi6_3 = 2.26183E-09
        sigmaf6_3 = 4.10284549E-02
        # Group 4 (Thermal)
        D6_4 = 0.260474712
        SigmaA6_4 = 0.274183869
        Sigmas6_34 = 0.161325693
        nuSigmaf6_4 = 0.373362422
        Chi6_4 = 3.96154E-11
        sigmaf6_4 = 1.00696474E-01
        
        # Group 1 Variables
        D_1 = [D0_1, D1_1, D2_1, D3_1, D4_1, D5_1, D6_1]
        SigmaR_1 = [SigmaR0_1, SigmaR1_1, SigmaR2_1, SigmaR3_1, SigmaR4_1, SigmaR5_1, SigmaR6_1]
        nuSigmaf_1 = [nuSigmaf0_1, nuSigmaf1_1, nuSigmaf2_1, nuSigmaf3_1, nuSigmaf4_1, nuSigmaf5_1, nuSigmaf6_1]
        Chi_1 = [Chi0_1, Chi1_1, Chi2_1, Chi3_1, Chi4_1, Chi5_1, Chi6_1]
        sigmaf_1 = [sigmaf0_1,sigmaf1_1,sigmaf2_1,sigmaf3_1,sigmaf4_1,sigmaf5_1,sigmaf6_1]
        # Group 2 Variables
        D_2 = [D0_2, D1_2, D2_2, D3_2, D4_2, D5_2, D6_2]
        SigmaA_2 = [SigmaR0_2, SigmaR1_2, SigmaR2_2, SigmaR3_2, SigmaR4_2, SigmaR5_2, SigmaR6_2]
        Sigmas_12 = [Sigmas0_12, Sigmas1_12, Sigmas2_12, Sigmas3_12, Sigmas4_12, Sigmas5_12, Sigmas6_12]
        nuSigmaf_2 = [nuSigmaf0_2, nuSigmaf1_2, nuSigmaf2_2, nuSigmaf3_2, nuSigmaf4_2, nuSigmaf5_2, nuSigmaf6_2]
        Chi_2 = [Chi0_2, Chi1_2, Chi2_2, Chi3_2, Chi4_2, Chi5_2, Chi6_2]
        sigmaf_2 = [sigmaf0_2,sigmaf1_2,sigmaf2_2,sigmaf3_2,sigmaf4_2,sigmaf5_2,sigmaf6_2]
        # Group 3 Variables
        D_3 = [D0_3, D1_3, D2_3, D3_3, D4_3, D5_3, D6_3]
        SigmaR_3 = [SigmaR0_3, SigmaR1_3, SigmaR2_3, SigmaR3_3, SigmaR4_3, SigmaR5_3, SigmaR6_3]
        Sigmas_23 = [Sigmas0_23, Sigmas1_23, Sigmas2_23, Sigmas3_23, Sigmas4_23, Sigmas5_23, Sigmas6_23]
        nuSigmaf_3 = [nuSigmaf0_3, nuSigmaf1_3, nuSigmaf2_3, nuSigmaf3_3, nuSigmaf4_3, nuSigmaf5_3, nuSigmaf6_3]
        Chi_3 = [Chi0_3, Chi1_3, Chi2_3, Chi3_3, Chi4_3, Chi5_3, Chi6_3]
        sigmaf_3 = [sigmaf0_3,sigmaf1_3,sigmaf2_3,sigmaf3_3,sigmaf4_3,sigmaf5_3,sigmaf6_3]
        # Group 4 Variables
        D_4 = [D0_4, D1_4, D2_4, D3_4, D4_4, D5_4, D6_4]
        SigmaA_4 = [SigmaA0_4, SigmaA1_4, SigmaA2_4, SigmaA3_4, SigmaA4_4, SigmaA5_4, SigmaA6_4]
        Sigmas_34 = [Sigmas0_34, Sigmas1_34, Sigmas2_34, Sigmas3_34, Sigmas4_34, Sigmas5_34, Sigmas6_34]
        nuSigmaf_4 = [nuSigmaf0_4, nuSigmaf1_4, nuSigmaf2_4, nuSigmaf3_4, nuSigmaf4_4, nuSigmaf5_4, nuSigmaf6_4]
        Chi_4 = [Chi0_4, Chi1_4, Chi2_4, Chi3_4, Chi4_4, Chi5_4, Chi6_4]
        sigmaf_4 = [sigmaf0_4,sigmaf1_4,sigmaf2_4,sigmaf3_4,sigmaf4_4,sigmaf5_4,sigmaf6_4]

        if dbg:print(time.time()-start)
        if dbg:print('~~~~Start Group 1 of 4~~~~')
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
        if dbg:print(time.time()-start)
        if dbg:print('~~~~Start Group 2 of 4~~~~')
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
        if dbg:print(time.time()-start)    
        if dbg:print('~~~~Start Group 3 of 4~~~~')   
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
        
        if dbg:print(time.time()-start)
        if dbg:print('~~~~Start Group 4 of 4~~~~')
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
            track_s.append(S)
            keff = kold*nm.sum(S)/nm.sum(Sold)
            track_k.append(keff)
            fluxdiff = abs((flux-fluxold)/flux)
            maxfluxdiff = fluxdiff.max()
            if dbg: print(time.time()-start,maxfluxdiff)
            
        
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
        if dbg: print('Core materials layout:')
        if dbg: print(LayoutSQ)
        if dbg: print('Flux of Fastest group (Group 1):')
        if dbg: print(fluxSQ_1)
        if dbg: print('Flux of Second Fastest group (Group 2):')
        if dbg: print(fluxSQ_2)
        if dbg: print('Flux of Second Slowest group (Group 3):')
        if dbg: print(fluxSQ_3)
        if dbg: print('Flux of Thermal group (Group 4):')
        if dbg: print(fluxSQ_4)
        if dbg: print('k = ', keff)
        if dbg: print('Elapsed time = ', elapsedtime, ' seconds')
        
        
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
        #if doPlot:
        #Create an 8x4 figure
        if dbg: print('Project3Code.solve plot 4 group flux')
        plt.clf()
        fig = plt.figure(1,(8.,8.))
        #Create an image grid obejct with 1 colorbar
        grid = ImageGrid(fig,111,nrows_ncols=(2,2),axes_pad=0.5,cbar_mode = 'single')#,aspect = False)#,cbar_mode='single')
        
        #Add plots
        g0 = grid[0].imshow(fluxSQ_1, vmin=0, vmax=maxv, cmap='jet', extent=[0, W, 0, H])
        grid[0].set_title('Group 1')
    
        #g0.set_title('Group 1')
        grid[1].imshow(fluxSQ_2, vmin=0, vmax=maxv, cmap='jet', extent=[0, W, 0, H])
        grid[1].set_title('Group 2')
    
        grid[2].imshow(fluxSQ_3, vmin=0, vmax=maxv, cmap='jet', extent=[0, W, 0, H])
        grid[2].set_title('Group 3')
    
        grid[3].imshow(fluxSQ_4, vmin=0, vmax=maxv, cmap='jet', extent=[0, W, 0, H])
        grid[3].set_title('Group 4')
        #Set colorbar scale
        grid.cbar_axes[0].colorbar(g0)
        if doSave:
            plt.savefig("%s_%sgroup.png"%(fn,4))
            #fig.canvas.draw()
        fig.canvas.draw()
        return track_k,fluxSQ_1,fluxSQ_2,fluxSQ_3,fluxSQ_4,track_s
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    