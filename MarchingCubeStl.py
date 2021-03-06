import matplotlib
import numpy
import pydicom
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import sys
import os

numpy.set_printoptions(threshold=sys.maxsize)

mypath = '../../Desktop/DICOM/10-26-2014-NA-PETCT SKULL-MIDTHIGH-30467/2.000000-CTAC-47844'
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
onlyfiles.sort()
model3DArray = []#Calling this initially as an empty list and then converting it to a numpy array at the end is the cleanest method of adding all necessary values
print(model3DArray)
for n in onlyfiles:
    
    model3DMask = numpy.ma.masked_less(pydicom.dcmread(mypath + '/' + n).pixel_array, int(700))
    model3DArray.append(model3DMask)
    #If imshow is repeatedly plotted it overlays it's data which is fine if all points are filled, but not fine if using a masked array

Final3DArray = numpy.array(model3DArray)
print(Final3DArray.shape[0])#z,_,_(x and y uknown order)
