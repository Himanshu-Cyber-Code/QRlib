from setuptools import setup
import sys

if sys.version_info < (3, 4, 0, 'final', 0):
    raise SystemExit('Python 3.4.0 or later is required !')
    
with open("README.md", "r") as file:
    long_description = file.read()
    
version = "1.0.0"
    
data={
    
    "name":"QRlib",
    
    "version":version,
    
    "author":"Himanshu Jha",
   
    "email":"ecxample@gmail.com",
    
    "license":"MIT",
    
    "required":[
        "requests",
        "tqdm",
        "urllib3",
        "svglib",
        ],
    
    "include_data":True,
    
    "console":[
        "QRlib=QRlib._cli:Cline"
        ],
    
    "url":"https://mjfv74xauzaho1ipyjadzg-on.drv.tw/QRlib/home.md",
    
    "pack":[
        "QRlib",
        ],
        
    "classifiers":[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    "description":{
        "short":"designer & trackable QR code generator ",
        "long":long_description,
        "type":"text/markdown",
    },
    
    "python_requires":">=3.4",
    
    }
     

setup(
    
    name = data["name"],
    
    version = data["version"],
    
    author = data["author"],
    
    author_email = data["email"],
    
    description = data["description"]["short"],
    
    long_description = data["description"]["long"],
    
    long_description_content_type = data["description"]["type"],
    
    url = data["url"],
    
    license = data["license"],
    
    packages = data["pack"],
    
    classifiers = data["classifiers"],
    
    python_requires = data["python_requires"],
    
    include_package_data = data["include_data"],
    
    install_requires = data["required"],
    
    entry_points = {"console_scripts":data["console"]},
)