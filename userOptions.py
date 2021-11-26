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

def marchingCubeRenderOption(path):
    mCRValues = ['Cutoff Values','Caps']
    mCRDict = {}
    validator = Validator.from_callable(is_number, error_message='This input contains non-numeric characters')
    for n in mCRValues:
        if n == 'Cutoff Values':
            userInput = prompt("Please input the options for the Marching Cube Render " + n + ': ', validator=validator)
        else:
            userInput = prompt("Please input the options for the Marching Cube Render " + n + ': ',)
        mCRDict[n] = userInput
    marchCubeRender(path,float(mCRDict['Cutoff Values']),mCRDict['Caps'] == 'True' or mCRDict['Caps'] == '1')

def STLExportOption(path):
    prompt("Please input the options for the STL Export: ")

def sliceViewOptions(path):
    sliceViewer(path)

def userOptionsMain(path):
    options = {'Marching Cube Render':marchingCubeRenderOption, 'STL Export':STLExportOption, 'Slice Viewer':sliceViewOptions} #Must call the function without () so that it doesn't immediatly call the function while setting up and instead later on we can use the function names to call the function

    userAutoCompleteList = WordCompleter(options.keys(), ignore_case=True)
    userDesire = prompt("Please input what you'd like to do: ", completer=userAutoCompleteList, validator=optionValidator(options.keys()))
    options[userDesire](path)
