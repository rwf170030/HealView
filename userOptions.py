from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError
from marchCubeRender import marchCubeRender
from sliceViewer import sliceViewer

class optionValidator(Validator):
    
    def __init__(self, optionsDictionaryInput):
        self.optionsDictionary = optionsDictionaryInput
    
    def validate(self, document):
        input = document.text
        if input not in self.optionsDictionary:
            raise ValidationError(message='This input is not an option')

def is_number(text):
    try:
        float(text)
        return True
    
    except:
        return False
    
def is_int(text):
    try:
        int(text)
        return True
    except:
        return False

def marchingCubeRenderOption(path):
    #mCRValues = ['Number of Cutoff Values','Cutoff Values','Caps']
    mCRDict = {}
    intValidator = Validator.from_callable(is_int, error_message='This input is not an integer')
    numValidator = Validator.from_callable(is_number, error_message='This input contains non-numeric characters')
    numCutoffValues = prompt("Please input the number of cutoff values you wish to have: ", validator=intValidator)
    cutoffValues = []
    
    while len(cutoffValues) < int(numCutoffValues):
        userInput = prompt("Please input a cutoff value you wish to use: ", validator=numValidator)
        cutoffValues.append(float(userInput))
    
    capsBool = prompt("Should the model to be capped on all sides: ")
    
    marchCubeRender(path,cutoffValues,capsBool.lower() in ['true', '1', 't', 'y', 'yes'])

def STLExportOption(path):
    prompt("Please input the options for the STL Export: ")

def sliceViewOptions(path):
    sliceViewer(path)

def userOptionsMain(path):
    options = {'Marching Cube Render':marchingCubeRenderOption, 'STL Export':STLExportOption, 'Slice Viewer':sliceViewOptions} #Must call the function without () so that it doesn't immediatly call the function while setting up and instead later on we can use the function names to call the function

    userAutoCompleteList = WordCompleter(options.keys(), ignore_case=True)
    userDesire = prompt("Please input what you'd like to do: ", completer=userAutoCompleteList, validator=optionValidator(options.keys()))
    options[userDesire](path)
