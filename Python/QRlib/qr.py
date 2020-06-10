
from . import _util as ql

def classic(qrdata, name, size=1000):
    for per in ql._percentbar([1,2,3,4,5,6,7], 'classic'):
        if per==1:
            ql._checkdata(qrdata, 'string', 'DATA FOR QR')
        if per==2:
            ql._checkdata(name, 'string', 'NAME FOR QR')
        if per==3:
            ql._checkdata(size, 0, 'SIZE FOR QR', _more=2000, _less=200)
        if per==4:
            configration = {"data":str(qrdata),"config":{"body":"square","logo":""},"size":int(size),"download":False,"file":"svg"}
        if per==5:
            svg = ql._reqmonkeyQR(url=0, data=configration)
        if per==6:
            ql._writesvg(svg,str(name))
        if per==7:
            ql._svg2png((str(name)+'.svg'),(str(name)))

def transparent(qrdata, name, img="", size=100):
    for per in ql._percentbar([1,2,3,4,5,6,7,8], 'transparent'):
        if per==1:
            ql._checkdata(qrdata, 'string', 'DATA FOR QR')
        if per==2:
            ql._checkdata(name, 'string', 'NAME FOR QR')
        if per==3:
            ql._checkdata(img, 'string', 'IMAGEURL')
        if per==4:
            ql._checkdata(size, 0, 'SIZE FOR QR', _less=100, _more=1000)
        if per==5:
            configration = {"data": str(qrdata),"image": str(img),"x": 0,"y": 0,"size": int(size),"crop": True,"download": False,"file": "svg"}
        if per==6:
            svg = ql._reqmonkeyQR(url=1, data=configration)
        if per==7:
            ql._writesvg(svg,str(name))
        if per==8:
            ql._svg2png((str(name)+'.svg'),(str(name)))
    
def custom(qrdata, name, body=6, frame=5, ball=7, bodycolor=(17, 49, 81), bgcolor=(255, 255, 255), ballcolor=(17, 49, 81), framecolor=(17, 49, 81), shadecolor=(17,49,81), shadeonball=True, shadetype=0, logo='', size=200):
    for per in ql._percentbar([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 'custom'):
        if per==1:
            ql._checkdata(qrdata, 'string', 'DATA FOR QR')
        if per==2:
            ql._checkdata(name, 'string', 'NAME FOR QR')
        if per==3:
            ql._checkdata(body, 0, 'BODY FOR QR', _less=0, _more=21)
        if per==4:
            ql._checkdata(frame, 0, 'FRAME FOR QR', _less=0, _more=16)
        if per==5:
            ql._checkdata(ball, 0, 'BALL FOR QR', _less=0, _more=19)
        if per==6:
            ql._checkdata(bodycolor, (0,0,0), 'BODY COLOUR FOR QR')
        if per==7:
            ql._checkdata(bgcolor, (0,0,0), 'BACK GROUND COLOUR FOR QR')
        if per==8:
            ql._checkdata(ballcolor, (0,0,0), 'BALL COLOUR FOR QR')
        if per==9:
            ql._checkdata(framecolor, (0,0,0), 'FRAME COLOUR FOR QR')
        if per==10:
            ql._checkdata(shadecolor, (0,0,0), 'SHADING COLOUR FOR QR')
        if per==11:
            ql._checkdata(shadeonball, True, 'IF WANT SHADE ON BALL')
        if per==12:
            ql._checkdata(logo, 'string', 'LOGO')
        if per==13:
            ql._checkdata(size, 0, 'SIZE FOR QR', _less=200, _more=2000)
        if per==14:
            ql._checkdata(shadetype, 0, 'TYPE OF SHADEING', _less=0, _more=1)
        if per==15:
            shadeformat={'0':'radial','1':'linear'}
        if per==16:
            shadetype1 = shadeformat[str(shadetype)]
        if per==17:
            designbody = {'0':'square','1':'mosaic','2':'dot','3':'circle','4':'circle-zebra','5':'circle-zebra-vertical','6':'circular','7':'edge-cut','8':'edge-cut-smooth','9':'japnese','10':'leaf','11':'pointed','12':'pointed-edge-cut','13':'pointed-in','14':'pointed-in-smooth','15':'pointed-smooth','16':'round','17':'rounded-in','18':'rounded-in-smooth','19':'rounded-pointed','20':'star','21':'diamond'}
            designframe = {'0':'frame0','1':'frame1','2':'frame10','3':'frame11','4':'frame12','5':'frame13','6':'frame14','7':'frame16','8':'frame2','9':'frame3','10':'frame4','11':'frame5','12':'frame6','13':'frame7','14':'frame8'}
            designball = {'0':'ball0','1':'ball1','2':'ball10','3':'ball11','4':'ball12','5':'ball13','6':'ball14','7':'ball15','8':'ball16','9':'ball17','10':'ball18','11':'ball19','12':'ball2','13':'ball3','14':'ball5','15':'ball6','16':'ball7','17':'ball8'}
        if per==18:
            _body = designbody[str(body)]
        if per==19:
            _frame = ('frame'+str(frame))
        if per==20:
            _ball = designball[str(ball)]
        if per==21:
            _bodycolor = ql._rgb2hex(bodycolor)
        if per==22:
            _bgcolor = ql._rgb2hex(bgcolor)
        if per==23:
            _framecolor = ql._rgb2hex(framecolor)
        if per==24:
            _ballcolor = ql._rgb2hex(ballcolor)
        if per==25:
            _shadecolor = ql._rgb2hex(shadecolor)
        if per==26:
            configration = {"data":str(qrdata),"config":{"body":str(_body),"eye":str(_frame),"eyeBall":str(_ball),"erf1":[],"erf2":["fh"],"erf3":["fv"],"brf1":[],"brf2":["fh"],"brf3":["fv"],"bodyColor":str(_bodycolor),"bgColor":str(_bgcolor),"eye1Color":str(_framecolor),"eye2Color":str(_framecolor),"eye3Color":str(_framecolor),"eyeBall1Color":str(_ballcolor),"eyeBall2Color":str(_ballcolor),"eyeBall3Color":str(_ballcolor),"gradientColor1":str(_bodycolor),"gradientColor2":str(_shadecolor),"gradientType":str(shadetype1),"gradientOnEyes":shadeonball,"logo":str(logo)},"size":int(size),"download":False,"file":"svg"}         
        if per==27:
            svg = ql._reqmonkeyQR(url=0, data=configration)
        if per==28:
            ql._writesvg(svg,str(name))
        if per==29:
            ql._svg2png((str(name)+'.svg'),(str(name)))
    
def clear(qrdata, name, size=1000):
    for per in ql._percentbar([1,2,3,4,5,6,7], 'clear'):
        if per==1:
            ql._checkdata(qrdata, 'string', 'DATA FOR QR')
        if per==2:
            ql._checkdata(name, 'string', 'NAME FOR QR')
        if per==3:
            ql._checkdata(size, 0, 'SIZE FOR QR', _less=100, _more=1000)
        if per==4:
            configration = {"data": str(qrdata),"image": "","x": 0,"y": 0,"size": int(size),"crop": True,"download": False,"file": "svg"}
        if per==5:
            svg = ql._reqmonkeyQR(url=1, data=configration)
        if per==6:
            ql._writesvg(svg,str(name))
        if per==7:
            ql._svg2png((str(name)+'.svg'),(str(name)))
    
def web(qrdata, name, tittle=''):
    for per in ql._percentbar([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 'web'):
        if per==1:
            ql._checkdata(qrdata, ['q','r'], 'WEB TEXT DATA FOR QR')
        if per==2:
            ql._checkdata(name, 'string', 'NAME FOR QR')
        if per==3:
            ql._checkdata(tittle, 'string', 'TITTLE FOR YOUR WEB TEXT')
        if per==4:
            temp0=0
        if per==5:
            for temp1 in qrdata:
                temp0=temp0+1
        if per==6:
            if(temp0>5):
                print(f"ERROR: webQR can't contain more than 5 lines and 1 tittle but you have given {str(temp0)} lines")
                sys.exit()
        if per==7:
            url='''https://himanshu-cyber-code.github.io/QRlib/HTML_support/Web_Text.html?'''
        if per==8:
            temp3=1
        if per==9:
            for temp2 in qrdata:
                url=(str(url)+'text'+str(temp3)+'='+ql._urlencode(str(temp2))+'&')
                temp3=temp3+1
        if per==10:
            url=str(url)+'text='+str(tittle)
        if per==11:
            weburl=('URL:'+ql._traceableurl(str(url)))
        if per==12:
            configration = {"data": str(weburl),"image": str("https://mjfv74xauzaho1ipyjadzg-on.drv.tw/QRlib/QRlib.png"),"x": 0,"y": 0,"size": 500,"crop": True,"download": False,"file": "svg"}
        if per==13:
            svg = ql._reqmonkeyQR(url=1, data=configration)
        if per==14:
            ql._writesvg(svg,str(name))
        if per==15:
            ql._svg2png((str(name)+'.svg'),(str(name)))
    
def fast_design(qrdata, name, json):
    ql._checkdata(qrdata, 'string', 'DATA FOR QR')
    ql._checkdata(name, 'string', 'NAME FOR QR')
    ql._checkdata(json, 'string', 'JSON FILE PATH')
    read = open(json, "r")
    jd=ql._readjson(read)
    custom(qrdata, name, body=jd['body'], frame=jd['frame'], ball=jd['ball'], bodycolor=jd['bodycolor'], bgcolor=jd['bgcolor'], ballcolor=jd['ballcolor'], framecolor=jd['framecolor'], shadecolor=jd['shadecolor'], shadeonball=jd['shadeonball'], shadetype=jd['shadetype'], logo=jd['logo'], size=jd['size'])
