import numpy
import vtk
import pydicom
import pyvista as pv
from filenameListGen import filelistGen

#X,Y,Z is based on horizontal axis of slice viewer, vertical axis of slice viewer, and layer slider in slice viewer respectively

def marchCubeRender(path, cutoffValueList, caps):
    onlyfiles = filelistGen(path)
    model3DArray = []#Calling this initially as an empty list and then converting it to a numpy array at the end is the cleanest method of adding all necessary values

    scale = [pydicom.dcmread(path + '/' + onlyfiles[0]).SliceThickness] #Z scaling
    scale.extend(pydicom.dcmread(path + '/' + onlyfiles[0]).PixelSpacing) #Order is row then column for matrix. should be y then x scaling. 
    
    for n in onlyfiles:
        model3DArray.append(pydicom.dcmread(path + '/' + n).pixel_array)
        #If imshow is repeatedly plotted it overlays it's data which is fine if all points are filled, but not fine if using a masked array

    data = numpy.array(model3DArray)
    if caps:
        capMatrixZ = data.min() * numpy.ones([1,numpy.size(data,1),numpy.size(data,2)]) #data axis goes from z,y,x with z being direction iterated in the loop, x and y being data present in a single image
        data = numpy.append(data, capMatrixZ, axis=0)
        data = numpy.insert(data, 0, data.min(), axis=0) #insert(array, position, newvalue, axis)
        capMatrixY = data.min() * numpy.ones([numpy.size(data,0),1,numpy.size(data,2)])#This goes along axis 1
        data = numpy.append(data, capMatrixY, axis=1)#Append when appending on the axis 1 for an array matches dimension for new array with current one (desired)
        data = numpy.insert(data, 0, data.min(), axis=1)#Insert when appending on the axis 1 for an array inserts entire new array each at each value for axis 1 dimension (not desired)
        capMatrixX = data.min() * numpy.ones([numpy.size(data,0),numpy.size(data,1),1])#This goes along axis 2
        data = numpy.append(data, capMatrixX, axis=2)
        data = numpy.insert(data, 0, data.min(), axis=2)
    
    data_vtk = pv.wrap(data)#This converts 3D array to pycista dat aobject which vtk can use

    mc = vtk.vtkMarchingCubes()
    mc.SetInputData(data_vtk)
    #a = 0
    #b = data.min()
    #b = 500 * round(b/500)
    #while b < data.max():
    a = 0
    
    for v in cutoffValueList:
        print(v)
        mc.SetValue(a,v)
        a+=1
    #    b = b + 500
    #    a = a + 1
    #    print(b)
    mc.Update()
    print(mc)
    polydata = mc.GetOutput()
    # points = dsa.WrapDataObject(polydata).Points
    print(polydata)
    mesh = pv.PolyData(polydata) #Convert marching cube update output to polydata
    mesh.scale(scale) #Scale by z,y,x
    print(mesh)
    p=pv.Plotter()
    actor = p.add_mesh(mesh, color='red')
    p.show()