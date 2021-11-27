import os

def filelistGen(path):
    onlyDICOMfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.dcm')]
    #f for _ means that the list values will be f for values in list if they abide by a condition. f is treated as the currently assesed value before finally being output as list. 
    #os path join joins the values in a manner that the os approves of in text. in our case it's joining the current path and the file from "f for" to see if the assesed path is a file and then if so it adds it to the output list.
    onlyDICOMfiles.sort()
    return onlyDICOMfiles