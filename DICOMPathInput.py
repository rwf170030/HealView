from prompt_toolkit import PromptSession
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.validation import Validator, ValidationError
import os

class FolderValidator(Validator):
    def validate(self, document):
        path = document.text
        if not os.path.isdir(path):
            raise ValidationError(message='This input is not a folder')
 
def getDICOMPath():
    userSession = PromptSession(history=FileHistory('.userHistory'))
    userAutoCompleteList = PathCompleter(only_directories=True)
    userInput = userSession.prompt("Select Folder For DICOM Processing: ", completer=userAutoCompleteList, validator=FolderValidator())
    return(userInput)