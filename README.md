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


| ![Classic QR](images/QR_sample_QRlib/classic.png) |
|:------:|
|    ```classic```    |


```python
from QRlib.QRlib import *

img_name = "ClassicQR" # name of Qr without extension of image ( default to png )
qr_data = "this is an classic qr" # content of qr
size = 200 # size in pixal ( optional )

qr.classic(qr_data, img_name, size=size)
```

___
###### *Tansparent QR*


| ![Transparent QR](images/QR_sample_QRlib/transparent.png) |
|:------:|
|    ```transparent```    |


```python
from QRlib.QRlib import *

img_name = "TransparentQR" # name of Qr without extension of image ( default to png )
qr_data = "this is an Transparent qr" # content of qr
img_url = "https://raw.githubusercontent.com/Himanshu-Cyber-Code/QRlib/master/images/QR_sample_QRlib/transparent_test.png" # url for the image ( optional )
size = 200 # size in pixal ( optional )

qr.transparent(qr_data, img_name, img=img_url, size=size)
```

-------


###### *Clear QR*


| ![Clear QR](images/QR_sample_QRlib/clear.png) |
|:------:|
|    ```clear```    |


```python
from QRlib.QRlib import *

img_name = "ClearQR" # name of Qr without extension of image ( default to png )
qr_data = "this is an Clear qr" # content of qr
size = 200 # size in pixal ( optional )

qr.clear(qr_data, qr_name, size=size)
```
-------
###### *Custom QR*

| ![CustomQR](images/QR_sample_QRlib/custom1.png "Sample Custom QR") |  | ![CustomQR](images/QR_sample_QRlib/custom2.png "Sample Custom QR") |  | ![CustomQR](images/QR_sample_QRlib/custom3.png "Sample Custom QR") |  | ![CustomQR](images/QR_sample_QRlib/custom4.png "Sample Custom QR") |  | ![CustomQR](images/QR_sample_QRlib/custom5.png "Sample Custom QR") |  |  ![CustomQR](images/QR_sample_QRlib/custom6.png "Sample Custom QR") |  | ![CustomQR](images/QR_sample_QRlib/custom7.png "Sample Custom QR") |  | ![CustomQR](images/QR_sample_QRlib/custom8.png "Sample Custom QR") |  |  ![CustomQR](images/QR_sample_QRlib/custom9.png "Sample Custom QR") |
|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
|    ```Custom_1```    |        |    ```Custom_2```    |        |    ```Custom_3```    |        |    ```Custom_4```    |        |    ```Custom_5```    |        |    ```Custom_6```    |        |    ```Custom_7```    |        |    ```Custom_8```    |        |    ```Custom_9```    |



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
body=6,  # Pattern Of QR Body
frame=5,  # Eye Frame Pattern
bodyc7,  # QR Eye Ball Pattern
bodycolor=(17, 49, 81),  # Colour For QR Body
bgcolor=(255, 255, 255),  # QR Back Ground Colour
ballcolor=(17, 49, 81),  # QR Eye Ball Colour
framecolor=(17, 49, 81),  # QR Frame Colour
shadecolor=(17, 49, 81),  # Colour Of Other  Shade Which Will Be Mix With Body Colour
shadeonball=True,  # If Shade Has To Be Applied On Eye Balls of Qr
shadetype=0,  # Type Of shade From Linear Or Radial
logo='https://raw.githubusercontent.com/Himanshu-Cyber-Code/QRlib/master/images/QR_sample_QRlib/transparent_test.png',  # Logo On Qr ( URL )
size=200 # Size For Qr
)
```


|  Body Design  |  No. |    |  Frame Design   |  No.   |     |  Ball Design  |  No.  |
|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
|    ![QRbody](images/QR_body_design_QRlib/0.png "Body Design")     |    0     |    |    ![QRframe](images/QR_frame_design_QRlib/0.png "Frame Design")     |    0     |    |    ![QRball](images/QR_ball_design_QRlib/0.png "Ball Design")     |    0     |
|    ![QRbody](images/QR_body_design_QRlib/1.png "Body Design")     |    1     |    |    ![QRframe](images/QR_frame_design_QRlib/1.png "Frame Design")     |    1     |    |    ![QRball](images/QR_ball_design_QRlib/1.png "Ball Design")     |    1     |
|    ![QRbody](images/QR_body_design_QRlib/2.png "Body Design")     |    2     |    |    ![QRframe](images/QR_frame_design_QRlib/2.png "Frame Design")     |    2     |    |    ![QRball](images/QR_ball_design_QRlib/2.png "Ball Design")     |    2     |
|    ![QRbody](images/QR_body_design_QRlib/3.png "Body Design")     |    3     |    |    ![QRframe](images/QR_frame_design_QRlib/3.png "Frame Design")     |    3     |    |    ![QRball](images/QR_ball_design_QRlib/3.png "Ball Design")     |    3     |
|    ![QRbody](images/QR_body_design_QRlib/4.png "Body Design")     |    4     |    |    ![QRframe](images/QR_frame_design_QRlib/4.png "Frame Design")     |    4     |    |    ![QRball](images/QR_ball_design_QRlib/4.png "Ball Design")     |    4     |
|    ![QRbody](images/QR_body_design_QRlib/5.png "Body Design")     |    5     |    |    ![QRframe](images/QR_frame_design_QRlib/5.png "Frame Design")     |    5     |    |    ![QRball](images/QR_ball_design_QRlib/5.png "Ball Design")     |    5     |
|    ![QRbody](images/QR_body_design_QRlib/6.png "Body Design")     |    6     |    |    ![QRframe](images/QR_frame_design_QRlib/6.png "Frame Design")     |    6     |    |    ![QRball](images/QR_ball_design_QRlib/6.png "Ball Design")     |    6     |
|    ![QRbody](images/QR_body_design_QRlib/7.png "Body Design")     |    7     |    |    ![QRframe](images/QR_frame_design_QRlib/7.png "Frame Design")     |    7     |    |    ![QRball](images/QR_ball_design_QRlib/7.png "Ball Design")     |    7     |
|    ![QRbody](images/QR_body_design_QRlib/8.png "Body Design")     |    8     |    |    ![QRframe](images/QR_frame_design_QRlib/8.png "Frame Design")     |    8     |    |    ![QRball](images/QR_ball_design_QRlib/8.png "Ball Design")     |    8     |
|    ![QRbody](images/QR_body_design_QRlib/9.png "Body Design")     |    9     |    |    ![QRframe](images/QR_frame_design_QRlib/9.png "Frame Design")     |    9     |    |    ![QRball](images/QR_ball_design_QRlib/9.png "Ball Design")     |    9     |
|    ![QRbody](images/QR_body_design_QRlib/10.png "Body Design")    |    10    |    |    ![QRframe](images/QR_frame_design_QRlib/10.png "Frame Design")    |    10    |    |    ![QRball](images/QR_ball_design_QRlib/10.png "Ball Design")    |    10    |
|    ![QRbody](images/QR_body_design_QRlib/11.png "Body Design")    |    11    |    |    ![QRframe](images/QR_frame_design_QRlib/11.png "Frame Design")    |    11    |    |    ![QRball](images/QR_ball_design_QRlib/11.png "Ball Design")    |    11    |
|    ![QRbody](images/QR_body_design_QRlib/12.png "Body Design")    |    12    |    |    ![QRframe](images/QR_frame_design_QRlib/12.png "Frame Design")    |    12    |    |    ![QRball](images/QR_ball_design_QRlib/12.png "Ball Design")    |    12    |
|    ![QRbody](images/QR_body_design_QRlib/13.png "Body Design")    |    13    |    |    ![QRframe](images/QR_frame_design_QRlib/13.png "Frame Design")    |    13    |    |    ![QRball](images/QR_ball_design_QRlib/13.png "Ball Design")    |    13    |
|    ![QRbody](images/QR_body_design_QRlib/14.png "Body Design")    |    14    |    |    ![QRframe](images/QR_frame_design_QRlib/14.png "Frame Design")    |    14    |    |    ![QRball](images/QR_ball_design_QRlib/14.png "Ball Design")    |    14    |
|    ![QRbody](images/QR_body_design_QRlib/15.png "Body Design")    |    15    |    |                                                                      |          |    |    ![QRball](images/QR_ball_design_QRlib/15.png "Ball Design")    |    15    |
|    ![QRbody](images/QR_body_design_QRlib/16.png "Body Design")    |    16    |    |                                                                      |          |    |    ![QRball](images/QR_ball_design_QRlib/16.png "Ball Design")    |    16    |
|    ![QRbody](images/QR_body_design_QRlib/17.png "Body Design")    |    17    |    |                                                                      |          |    |    ![QRball](images/QR_ball_design_QRlib/17.png "Ball Design")    |    17    |
|    ![QRbody](images/QR_body_design_QRlib/18.png "Body Design")    |    18    |    |                                                                      |          |    |                                                                   |          |
|    ![QRbody](images/QR_body_design_QRlib/19.png "Body Design")    |    19    |    |                                                                      |          |    |                                                                   |          |
|    ![QRbody](images/QR_body_design_QRlib/20.png "Body Design")    |    20    |    |                                                                      |          |    |                                                                   |          |
|    ![QRbody](images/QR_body_design_QRlib/21.png "Body Design")    |    21    |    |                                                                      |          |    |                                                                   |          |


___
###### Web Qr


| ![WebQR](images/QR_sample_QRlib/Web.png) | ![WebQRScreen](images/QR_sample_QRlib/WebQR_Screenshot.jpg) |
|:------:|:------:|
|    ```Web QR```    |    [Link In QR](https://is.gd/mczMv4)    |


```python
# Web QR are online And Can Be Used In Track Data To Get Trackable QR ( Details On Track Data Bellow )
from QRlib.QRlib import *

img_name = "WebQR" # name of Qr without extension of image ( default to png )
qr_data = ["line 1", "line 2", "line 3", "line 4", "line 5"] # content of web qr should be list of string each string represents line break ( maximum line is 5 )
tittle = "i am tittle" # tittle of the web page ( optional )

qr.web(qr_data, img_name, tittle=tittle)
```

