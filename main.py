import time

'''
Required Milestones:
1. Library for Data Classification and Extraction
 - the documents must be identified, classified, and divided
    into multiple groups
    submit a single file (image/pdf/word document)
    that contains many documents.
    To achieve:
    1. Class Extract
    2. Relevant Docstrings
    3. Implement functions in class - identify(take input and OCR function), save, 
        OCR Function(conditions for diff documents and split based result)

2. Once document is classified and split, create a library which accepts split
document and extracts the data from it.

Non-Tech Issues
1. Project README
2. Docstring for Functions
3. Find which all functions can be added to improve efficiency and workflow
'''

class Xtractor:
    # Milestone 1
    def __init__(self):
        '''
        Based on the input file, the documents must be identified, classified, and divided
        into multiple groups. Library that accepts a user supplied file and
        recognises and splits numerous documents existing in the file.
        '''
        pass
    
    # For OCR and identify, either single file can be given or a filepath will be given
    def OCR(self, filepath=None, filename=None, **kwargs):
        print("OCR Performed")
        return True

    
    # identify funtion uses OCR to identify documents and returns type of each
    def identify(self, filepath=None, filename=None, **kwargs):
        pass 
    
    # Save the output at a location
    def save(self, outputlocation, **kwargs):
        pass

    # Milestone 2
    # Extract Data from doc and return it as text
    def extractData(self, filepath=None, filename=None, **kwargs):
        pass