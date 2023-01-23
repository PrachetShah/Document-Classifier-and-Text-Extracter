from paddleocr import PaddleOCR, draw_ocr
import os
import cv2
import numpy as np
# import matplotlib.pyplot as plt


class Xtracter:
    # Milestone 1
    def __init__(self):
        '''
        Based on the input file, the documents must be identified, classified, and divided
        into multiple groups. Library that accepts a user supplied file and
        recognises and splits numerous documents existing in the file.
        '''
        pass
    
    # For OCR and identify, either single file can be given or a filepath will be given
    def OCR(self, filepath=None, filename=None, outpath=None,**kwargs):
        # Defining our OCR and specify font for it
        ocr = PaddleOCR(use_angle_cls=True)
        
        # Specifying output path and font path.
        # if outpath:
        #     out_path = './'
        # else:
        out_path = './output_images'
        font = 'simfang.ttf'

        result = ocr.ocr('aadhaar2.jpg')
        for line in result[0]:
            print(line[1][0])
        
        print("OCR Performed")
        return result

    
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


# trial = Xtracter()
ocr = PaddleOCR(use_angle_cls=True, use_gpu=False)
out_path = './output_images'
font = 'simfang.ttf'

result = ocr.ocr('aadhaar2.jpg')
for line in result[0]:
    print(line[1][0])

print("OCR Performed")
result = ocr.OCR(filepath='aadhaar2.jpg')