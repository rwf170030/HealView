import pydicom
from filenameListGen import filelistGen

path = '../../Desktop/DICOM/10-26-2014-NA-PETCT SKULL-MIDTHIGH-30467/2.000000-CTAC-47844'
filenames = filelistGen(path)
print(pydicom.dcmread(path + '/' + filenames[0]).PixelSpacing)
print(pydicom.dcmread(path + '/' + filenames[27]).SliceThickness)