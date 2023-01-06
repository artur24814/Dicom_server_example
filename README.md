# Dicom_server_example

![PyDicom](https://img.shields.io/badge/-PyDicom-black?style=for-the-badge&logo=Python)
![PyNetDicom](https://img.shields.io/badge/-PyNetDicom-black?style=for-the-badge&logo=Python)<br>

<img src='https://www.endpointadjudication.com/-/media/Project/endpoint-adjudication/images/blog/using-DICOM-Viewers-in-eAdjudication-desktop.ashx' />

## Contents
 * <a href="#info"><strong>Info</strong></a><p>Information about the resources used in this project</p>
 * <a href="#winamp"><strong>Server Dicom</strong></a><p>A simple example of dicom server with using PyNetDicom</p>
 * <a href="#clone_project"><strong>Clone and Run Project</strong></a><p>how run projects in your computer</p>

<hr>

<details><summary id="info" style="font-size: 30px;"> INFO</summary>
<h4>Information about the additional library, external Api used in this project and general information</h4>

<strong>PyQt5</strong> PyQt5 is a comprehensive set of Python bindings for Qt v5.

<strong>pyqt5-tools</strong> The PyQt5 wheels do not provide tools such as Qt Designer that were included in the old binary installers. This package aims to provide those in a separate package which is useful for developers while the official PyQt5 wheels stay focused on fulfilling the dependencies of PyQt5 applications.

</details>

<hr>
<center><h1 id="winamp"> Server Dicom <span style='font-size:80px;'><img src="https://pydicom.github.io/pynetdicom/stable/_static/pydicom_flat_black.svg" width='30' heigth='30'/></span></h1></center>



DICOM® — Digital Imaging and Communications in Medicine — is the international standard for medical images and related information. It defines the formats for medical images that can be exchanged with the data and quality necessary for clinical use.

DICOM® is implemented in almost every radiology, cardiology imaging, and radiotherapy device (X-ray, CT, MRI, ultrasound, etc.), and increasingly in devices in other medical domains such as ophthalmology and dentistry. With hundreds of thousands of medical imaging devices in use, DICOM® is one of the most widely deployed healthcare messaging Standards in the world. There are literally billions of DICOM® images currently in use for clinical care.

Since its first publication in 1993, DICOM® has revolutionized the practice of radiology, allowing the replacement of X-ray film with a fully digital workflow. Much as the Internet has become the platform for new consumer information applications, DICOM® has enabled advanced medical imaging applications that have “changed the face of clinical medicine”. From the emergency department, to cardiac stress testing, to breast cancer detection, DICOM® is the standard that makes medical imaging work — for doctors and for patients.

DICOM® is recognized by the International Organization for Standardization as the ISO 12052 standard.

read more from <a href="https://www.dicomstandard.org/" target="_blank" >official dicom standard website</a>

<center><h2 id="clone_project">Clone and Run a Project</h2></center>


To start, we need to clone my project from Github:-
<p>Above the list of files, click Code.</p>
<img src="https://docs.github.com/assets/cb-20363/images/help/repository/code-button.png">

Copy the URL for the repository.
<ul>
<li>To clone the repository using HTTPS, under "HTTPS", click</li>
<li>To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click</li>
<li>To clone a repository using GitHub CLI, click GitHub CLI, then click</li>
</ul>
<img src="https://docs.github.com/assets/cb-33207/images/help/repository/https-url-clone-cli.png">

Open Terminal.

Change the current working directory to the location where you want the cloned directory.

Type git clone, and then paste the URL you copied earlier.

`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

Press Enter to create your local clone.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...<br>
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Before diving let’s look at the things we are required to install in our system.

To run App prefer to use the Virtual Environment

`pip install virtualenv`

Making and Activating the Virtual Environment:-

`virtualenv “name as you like”`

`source “name as you like”/bin/activate`

Install the project dependencies:

`pip install -r requirements.txt`

to run

`python Start.py`



Have fun
<p style="font-size:100px">&#129409;</p>
