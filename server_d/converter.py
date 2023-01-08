import pydicom
import os
import numpy as np
from PIL import Image


class ConverterDicom:
    available_formats = ['PNG', 'JPG', 'DCM']
    dicom_files = False

    def __init__(self, path_dicom, files):
        self.path_dicom = path_dicom
        self.path_files = self.check_files(files)

    def check_files(self, files):
        #get format from path
        format = files.split('.')[-1].upper()
        #check format
        if format not in self.available_formats:
            raise TypeError('unsupported format')
        elif format == 'DCM':
            self.dicom_files = True
            # find directiries in path
            directories = files.split('/')
            if len(directories) != 1:
                # create directories from list
                self.create_directories(directories)

            return files
        else:
            #find directiries in path
            directories = files.split('/')
            if len(directories) != 1:
                #create directories from list
                self.create_directories(directories)

            return files

    def convert_to_global_path(self):
        self.convert(global_path=True)

    def convert(self, global_path=False):
        #read dicom file
        ds = pydicom.dcmread(self.path_dicom)
        #create new file from pixel array
        new_image = ds.pixel_array.astype(float)
        #rescale its pixels and put their values between 0 and 255.
        scaled_image = (np.maximum(new_image, 0) / new_image.max()) * 255.0
        #convert it into 8 bits unsigned integer.
        scaled_image = np.uint8(scaled_image)
        #finaly create image from array
        final_image = Image.fromarray(scaled_image)
        #save image
        if global_path:
            final_image.save(self. path_files)
        else:
            path = os.path.join(os.getcwd(), self.path_files)
            final_image.save(path)

    def create_directories(self, directories):
        current_dir = os.getcwd()
        for directory in directories[:-1]:
            #cath existingdir error
            try:
                #change current dir
                current_dir = os.path.join(current_dir, directory)
                #make dir
                os.mkdir(current_dir)
            except Exception as e:
                print(e)

    def create_pdf(self):
        pass

    def change_dataset(self, list_elements, list_values):
        if self.dicom_files:
            try:
                ds = pydicom.dcmread(self.path_dicom)
                #check if quantity elements equal values
                if len(list_elements) == len(list_values):
                    for element in list_elements:
                        ds.__dict__[f'{element}'] = list_values[list_elements.index(element)]
                ds.save_as(self.path_files)
            except Exception as e:
                print("Error dataset", e)
        else:
            print('Not dicom format')