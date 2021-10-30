import matplotlib
import numpy
import pydicom
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


import os

mypath = '../../Desktop/DICOM/10-26-2014-NA-PETCT SKULL-MIDTHIGH-30467/2.000000-CTAC-47844'
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
onlyfiles.sort()
model3DArray = pydicom.dcmread(mypath + '/' + '1-119.dcm').pixel_array

fig = plt.figure()
ax = fig.subplots()

plotFigure = ax.imshow(model3DArray)

ax_slide = plt.axes([0.9,0.1,0.05,0.8]) #xpos,ypos,width,height

s_factor = matplotlib.widgets.Slider(ax_slide, 'Cutoff Point', valmin = model3DArray.min(), valmax = model3DArray.max(), valinit = model3DArray.min(), valstep = 1, orientation = 'vertical')

def plotUpdate(val):
    print(val)
    model3DMask = numpy.ma.masked_less_equal(model3DArray, s_factor.val, copy=True)
    plt.imshow(model3DMask)
    fig.canvas.draw()


s_factor.on_changed(plotUpdate)

plt.show()