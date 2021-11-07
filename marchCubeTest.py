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
    model3DArray.append(pydicom.dcmread(mypath + '/' + n).pixel_array)
    #If imshow is repeatedly plotted it overlays it's data which is fine if all points are filled, but not fine if using a masked array

data = numpy.array(model3DArray)

data_vtk = pv.wrap(data)#This converts 3D array to vtk data with the pv library

mc = vtk.vtkMarchingCubes()
mc.SetInputData(data_vtk)
#a = 0
#b = data.min()
#b = 500 * round(b/500)
#while b < data.max():
mc.SetValue(0,700)
#    b = b + 500
#    a = a + 1
#    print(b)
mc.Update()
print(mc)
polydata = mc.GetOutput()
# points = dsa.WrapDataObject(polydata).Points
print(polydata)
mesh = pv.PolyData(polydata)
print(mesh)
p=pv.Plotter()
actor = p.add_mesh(mesh, color='red')
p.show()
