import numpy
import vtk
import pydicom
import os
import pyvista as pv

def marchCubeRender(path, cutoffValue, caps):
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    onlyfiles.sort()
    model3DArray = []#Calling this initially as an empty list and then converting it to a numpy array at the end is the cleanest method of adding all necessary values

    print(model3DArray)
    for n in onlyfiles:
        model3DArray.append(pydicom.dcmread(path + '/' + n).pixel_array)
        #If imshow is repeatedly plotted it overlays it's data which is fine if all points are filled, but not fine if using a masked array

    data = numpy.array(model3DArray)
    if caps:
        capMatrix = data.min() * numpy.ones((1,numpy.size(data,1),numpy.size(data,2))) #data axis goes from z,y,x with z being direction iterated in the loop, x and y being data present in a single image
        data = numpy.append(data, capMatrix, axis=0)
        data = numpy.insert(data, 0, capMatrix, axis=0)
    
    data_vtk = pv.wrap(data)#This converts 3D array to vtk data with the pv library

    mc = vtk.vtkMarchingCubes()
    mc.SetInputData(data_vtk)
    #a = 0
    #b = data.min()
    #b = 500 * round(b/500)
    #while b < data.max():
    mc.SetValue(0,cutoffValue)
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