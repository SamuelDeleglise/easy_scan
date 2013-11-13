import scan
import os


kwds = {'lambda_um':1.064,
       'llambda':1.,
       't':0.2,
       'n_r':3.48,
       'eta':0.7,
       'n_orders':3,
       'pol':'TE'}

os.chdir("D:/Dropbox/Theorie/grattings/RCWA/rodis/data")

kwds['eta'] = 0.7
s = scan.ScanBeam('t', 0.1,3., 400,'lambda_um', 0.1,3.,400,**kwds)
s.calc()
s.save()
kwds['eta'] = 0.8
s = scan.ScanBeam('t', 0.1,0.9, 100,'lambda_um', 0.1,1.1,100,**kwds)
s.calc()
s.save()
#kwds['llambda'] = 0.8
#s = scan.ScanBeam('eta', 0.1,0.9, 100,'lambda_um', 0.1,1.1,100,**kwds)
#s.calc()
#s.save()
#kwds['llambda'] = 0.7
#s = scan.ScanBeam('eta', 0.1,0.9, 100,'lambda_um', 0.1,1.1,100,**kwds)
#s.calc()
#s.save()

import interactive_gratting