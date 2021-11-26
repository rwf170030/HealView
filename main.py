import os
import sys
from DICOMPathInput import getDICOMPath
from userOptions import userOptionsMain


#sys.argv[0] = path, 1 = input 
try:
    if os.path.isdir(sys.argv[1]):
        Path = sys.argv[1]
except:
    Path = getDICOMPath()
    
userOptionsMain(Path)
