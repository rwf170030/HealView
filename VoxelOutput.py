import numpy
import vtk
import pydicom
import os
import pyvista as pv
from vtk.util import numpy_support
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
# from vtk.numpy_interface import dataset_adapter as dsa
colors = vtkNamedColors()


mypath = '../../Desktop/DICOM/10-26-2014-NA-PETCT SKULL-MIDTHIGH-30467/2.000000-CTAC-47844'
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
onlyfiles.sort()
model3DArray = []#Calling this initially as an empty list and then converting it to a numpy array at the end is the cleanest method of adding all necessary values
print(model3DArray)
for n in onlyfiles:
    model3DMask = pydicom.dcmread(mypath + '/' + n).pixel_array
    model3DArray.append(model3DMask)
    #If imshow is repeatedly plotted it overlays it's data which is fine if all points are filled, but not fine if using a masked array

data = numpy.array(model3DArray)

print(model3DMask)
data_vtk = pv.wrap(data)
p=pv.Plotter()
p.add_mesh_threshold(data_vtk)
p.show()