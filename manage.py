import argparse
from converter import ConverterDicom

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dicom_image", help="path to dicom image")
parser.add_argument("-c", "--convert", help="convert to image, your argument will be a path were image will save")
parser.add_argument("-g", "--global_path", help="save in global path, not inside project")
parser.add_argument("-u", "--update_ds", help="update dataset, provide list of elements")
parser.add_argument("-v", "--value_ds", help="update dataset, provide list of values")

args = parser.parse_args()

if __name__ == '__main__':
    # if argument for start server
    if args.dicom_image and args.convert and args.update_ds and args.value_ds:
        # catch error from checking file output path
        try:
            c = ConverterDicom(args.dicom_image, args.convert)
            c.change_dataset(args.update_ds, args.value_ds)
        except TypeError as error:
            print(error)
    elif args.dicom_image and args.convert or args.dicom_image and args.convert and args.global_path:
        # catch error from checking file output path
        try:
            c = ConverterDicom(args.dicom_image, args.convert)
            c.convert()
        except TypeError as error:
            print(error)

    else:
        parser.print_help()