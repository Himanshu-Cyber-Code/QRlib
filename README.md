# QRlib

QRlib is an pure python qr code generator which can be used to create simple QR code , designer QR code or trackable QR codes


## What is a QR Code?


A Quick Response code is a two-dimensional pictographic code used for its fast readability and comparatively large storage capacity. The basic QR code consists of black modules arranged in a square pattern on a white background. The information encoded can be made up of any kind of data (e.g., binary, alphanumeric, or Kanji symbols).


## Installation


you can install QRlib with pip command
```bash
pip install QRlib
```
or with pip3
```bash
pip3 install QRlib
```

## Requirements


* python 3.4 or above
* [requests module](https://pypi.org/project/requests/)
* [tqdm module](https://pypi.org/project/tqdm/)
* [svglib module](https://pypi.org/project/svglib/)
* [reportlab module](https://pypi.org/project/reportlab/)
* [urllib module](https://pypi.org/project/urllib3/)

## Command Line Arguments
* ##### to update QRlib to latest version
    * ```python -m QRlib --update```

    * ```python -m QRlib -u```
* ##### to get help on module QRlib
    * ```python -m QRlib --help```
 
    * ```python -m QRlib -h```

## Importing QRlib


import QRlib with command
```python
from QRlib.QRlib import *
```

## Generating QR codes

###### *Classic QR*
![Classic QR](classicQR.png
```python
from QRlib.QRlib import *

img_name = "ClassicQR" # name of Qr without extension of image ( default to png )
qr_data = "this is an classic qr" # content of qr
size = 200 # size in pixal ( optional )

qr.classic(qr_data, img_name, size=size)
```

 ___
###### *Tansparent QR*
![Transparent QR](transparentQR.png
```python
from QRlib.QRlib import *

img_name = "TransparentQR" # name of Qr without extension of image ( default to png )
qr_data = "this is an Transparent qr" # content of qr
img_url = "https://9p933al7lphdqzqhwh4gbg-on.drv.tw/QRlib/transtest.png" # url for the image ( optional )
size = 200 # size in pixal ( optional )

qr.transparent(qr_data, img_name, img=img_url, size=size)
```

-------


###### *Clear QR*
![Clear QR](clearQR.png
```python
from QRlib.QRlib import *

img_name = "ClearQR" # name of Qr without extension of image ( default to png )
qr_data = "this is an Clear qr" # content of qr
size = 200 # size in pixal ( optional )

qr.clear(qr_data, qr_name, size=size)
```
-------
###### *Custom QR*

| ![Custom QR](custom1QR.png
|:------:|
|    ```Custom_1```    |

| ![Custom QR](custom2QR.png
|:------:|
|    ```Custom_2```    |

| ![Custom QR](custom3QR.png
|:------:|
|    ```Custom_3```    |

| ![Custom QR](custom4QR.png
|:------:|
|    ```Custom_4```    |

| ![Custom QR](custom5QR.png
|:------:|
|    ```Custom_5```    |

| ![Custom QR](custom6QR.png
|:------:|
|    ```Custom_6```    |

| ![Custom QR](custom7QR.png
|:------:|
|    ```Custom_7```    |

| ![Custom QR](custom8QR.png
|:------:|
|    ```Custom_8```    |

| ![Custom QR](custom9QR.png
|:------:|
|    ```Custom_9```    |

And +1000 More Design`s

```python
# An Minimum Example

from QRlib.QRlib import *

img_name = "CustomQR" # name of Qr without extension of image ( default to png )
qr_data = "this is an Custom qr" # content of qr

qr.custom(qr_data, qr_name)
```

```python
# An Maximum Example

from QRlib.QRlib import *

img_name = "CustomQR" # name of Qr without extension of image ( default to png )
qr_data = "this is an Custom qr" # content of qr

qr.custom(
qr_data,
qr_name, 
body=5,  # Pattern Of QR Body
frame=13,  # Eye Frame Pattern
ball=15,  # QR Eye Ball Pattern
bodycolor=(148,143,32),  # Colour For QR Body
bgcolor=(255,255,255),  # QR Back Ground Colour
ballcolor=(26,26,56),  # QR Eye Ball Colour
framecolor=(3,190,242),  # QR Frame Colour
shadecolor=(41,136,161),  # Colour Of Other  Shade Which Will Be Mix With Body Colour
shadeonball=True,  # If Shade Has To Be Applied On Eye Balls of Qr
shadetype=0,  # Type Of shade From Linear Or Radial
logo='',  # Logo On Qr ( URL )
size=200 # Size For Qr
)
```


|  Body Design  |  No. |
|:------:|:------:|
|    ![QRbody](/images/QR_body_design_QRlib/0.png "Body Design")    |    0    |
|    ![QRbody](/images/QR_body_design_QRlib/1.png "Body Design")    |    1    |
|    ![QRbody](/images/QR_body_design_QRlib/2.png "Body Design")    |    2    |
|    ![QRbody](/images/QR_body_design_QRlib/3.png "Body Design")    |    3    |
|    ![QRbody](/images/QR_body_design_QRlib/4.png "Body Design")    |    4    |
|    ![QRbody](/images/QR_body_design_QRlib/5.png "Body Design")    |    5    |
|    ![QRbody](/images/QR_body_design_QRlib/6.png "Body Design")    |    6    |
|    ![QRbody](/images/QR_body_design_QRlib/7.png "Body Design")    |    7    |
|    ![QRbody](/images/QR_body_design_QRlib/8.png "Body Design")    |    8    |
|    ![QRbody](/images/QR_body_design_QRlib/9.png "Body Design")    |    9    |
|    ![QRbody](/images/QR_body_design_QRlib/10.png "Body Design")    |    10    |
|    ![QRbody](/images/QR_body_design_QRlib/11.png "Body Design")    |    11    |
|    ![QRbody](/images/QR_body_design_QRlib/12.png "Body Design")    |    12    |
|    ![QRbody](/images/QR_body_design_QRlib/13.png "Body Design")    |    13    |
|    ![QRbody](/images/QR_body_design_QRlib/14.png "Body Design")    |    14    |
|    ![QRbody](/images/QR_body_design_QRlib/15.png "Body Design")    |    15    |
|    ![QRbody](/images/QR_body_design_QRlib/16.png "Body Design")    |    16    |
|    ![QRbody](/images/QR_body_design_QRlib/17.png "Body Design")    |    17    |
|    ![QRbody](/images/QR_body_design_QRlib/18.png "Body Design")    |    18    |
|    ![QRbody](/images/QR_body_design_QRlib/19.png "Body Design")    |    19    |
|    ![QRbody](/images/QR_body_design_QRlib/20.png "Body Design")    |    20    |
|    ![QRbody](/images/QR_body_design_QRlib/21.png "Body Design")    |    21    |





___
###### Web Qr






















