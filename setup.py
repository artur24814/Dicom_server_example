from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = ' Dicom server example'
LONG_DESCRIPTION = 'A simple example of dicom server with using PyNetDicom.'

# Setting up
setup(
    name="server-d",
    version=VERSION,
    author="artur24814",
    author_email="artur24814@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pydicom', 'pynetdicom', 'Pillow', 'numpy'],
    keywords=['pydicom', 'server', 'pynetdicom', 'convert dicom'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)