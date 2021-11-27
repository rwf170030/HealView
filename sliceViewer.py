import matplotlib
import numpy
import pydicom
import matplotlib.pyplot as plt
from filenameListGen import filelistGen

def sliceViewer(path):
    onlyfiles = filelistGen(path)
    model3DArray = []#Calling this initially as an empty list and then converting it to a numpy array at the end is the cleanest method of adding all necessary values
    
    scale=pydicom.dcmread(path + '/' + onlyfiles[0]).PixelSpacing #Order is row then column for matrix. should be y then x scaling
    
    for n in onlyfiles:
        model3DArray.append(pydicom.dcmread(path + '/' + n).pixel_array)
        #if n == '1-120.dcm':
        #    model3DArray.append(pydicom.dcmread(path + '/' + n).pixel_array)
        #if n == '1-120.dcm':
        #    model3DArray.append(pydicom.dcmread(path + '/' + n).pixel_array)
    Final3DArray = numpy.array(model3DArray)
    print(Final3DArray.shape[0])#z,_,_(x and y uknown order)

    fig = plt.figure()
    plottedSubplot = fig.subplots()
    plotFigure = plottedSubplot.imshow(Final3DArray[0], cmap = plt.get_cmap('Greys'), aspect = (scale[0]/scale[1]))


    ax_slide = plt.axes([0.875,0.1,0.05,0.8]) #xpos,ypos,width,height
    ax_slide2 = plt.axes([0.075,0.1,0.05,0.8]) #xpos,ypos,width,height

    s_factor = matplotlib.widgets.Slider(ax_slide, 'Cutoff Point', valmin = Final3DArray.min(), valmax = Final3DArray.max(), valinit = Final3DArray.min(), valstep = 1, orientation = 'vertical')
    s_factor2 = matplotlib.widgets.Slider(ax_slide2, 'Current Layer', valmin = 0, valmax = Final3DArray.shape[0] - 1, valinit = 0, valstep = 1, orientation = 'vertical')

    def plotUpdate(val):
        print(val)
        maskedDisplayLayer = numpy.ma.masked_less(Final3DArray[s_factor2.val], int(s_factor.val))
        #If imshow is repeatedly plotted it overlays it's data which is fine if all points are filled, but not fine if using a masked array
        plotFigure.set_data(maskedDisplayLayer)
        


        fig.canvas.draw()

    s_factor.on_changed(plotUpdate)
    s_factor2.on_changed(plotUpdate)

    plt.show()