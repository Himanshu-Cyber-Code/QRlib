import requests
import json
from datetime import datetime
import urllib.parse
import sys
import os
from tqdm import tqdm
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

def _svg2png(_svgfile, _name):
    drawing = svg2rlg(_svgfile)
    renderPM.drawToFile(drawing, (str(_name)+".png"), fmt="PNG")
    os.remove(str(_name)+".svg")
    
def _checkdata(_data, _type, _name, _equal=None, _more=None, _less=None):
    if(type(_data)!=type(_type)):
        print(f'ERROR:expected an {type(_type)} value in {_name} field but you have given an {type(_data)}')
        sys.exit()
    if(_equal!=None):
        if(_data not in _equal):
            print(f'ERROR:{_data} is not a valid input here it should be from [{_equal}]')
            sys.exit()
    if(_more!=None):
        if(_data>_more):
            print(f"ERROR:{_name} can't be more than {_more} but you have given {_data}")
            sys.exit()
    if(_less!=None):
        if(_data<_less):
            print(f"ERROR:{_name} can't be less than {_less} but you have given {_data}")
            sys.exit()

def _rgb2hex(rgb):
    return ('#'+'%02x%02x%02x' % rgb)

def _writesvg(svgdata,name):
    nametemp = (str(name)+'.svg')
    text_file = open(nametemp, "w")
    text_file.write(str(svgdata))
    text_file.close()

def _nowtimedate():
	now = datetime.now()
	ndy = now.strftime("%Y")
	ndm = now.strftime("%m")
	ndd = now.strftime("%d")
	nth = now.strftime("%H")
	ntm = now.strftime("%M")
	return [int(ndy),int(ndm),int(ndd),int(nth),int(ntm)]
	
def _shorturl(url, data=False):
    web = f'https://is.gd/create.php?url={url}&shorturl=&format=simple'
    response = requests.post(web)
    surl = response.text
    temp1 = 0
    temp2 = 0
    for temp3 in surl :
    	
	    temp2 = temp2+1
	    if(temp3=='/'):
	    	temp1 = temp1+1
	    if(temp1==3):
		    break
    surldata=url[int(temp2):int(len(url))]
    if (data):
        return surldata
    else:
        return surl
    
def _geturldata(url):
    surl = str(url)
    temp1 = 0
    temp2 = 0
    for temp3 in surl:
	    temp2 = temp2+1
	    if(temp3=='/'):
		    temp1 = temp1+1
	    if(temp1==3):
		    break
    surldata = url[int(temp2):int(len(url))]
    return surldata
    
def _verifyemail(email):
    check = 0
    temp1 = ''
    for i in email[::-1]:
	    if i=='@':
		    break
	    temp1 = temp1+i
    temp1 = temp1[::-1]
    temp1 = temp1.replace('.', ' .......... ')
    if ' .......... ' not in temp1:
	    check = check+1
    g = email
    val = 0
    for i in g:
	    if i=='@':
		    val=val+1
    if val==0:
	    check=check+1
    g = g[::-1]
    g = g[g.find('@')+1:]
    g = g[::-1]
    if len(g)==0:
	    check=check+1
    data1 = g+'@'
    g = email
    temp2 = email
    val = 0
    for i in g:
	    if i=='.':
		    val = val+1
    if val==0:
	    check=check+1
    g = g[::-1]
    g = g[g.find('.')+1:]
    g = g[::-1]
    g = temp2.replace(g+'.','')
    if len(g)==0:
	    check = check+1
    data2='.'+g
    g = email
    g = g.replace(data1,'')
    g = g.replace(data2,'')
    if len(g)==0:
        check=check+1
    if(check!=0):
        print(f'ERROR:your entered email {email} is not a valid one')
        sys.exit()
        
def _str2json(data):
    return json.dumps(data)
    
def _reqmonkeyQR(url=None, data=None):
    urls = {'0':'https://qr-generator.qrcode.studio/qr/custom','1':'https://generator.qrcode.studio/qr/transparent','2':'0000000000'}
    response = requests.post(urls[str(url)], json=data, headers={'content-type': 'application/json','Accept':'image/svg'})
    return response.text
    
def _urlencode(data):
    return urllib.parse.quote(data)
        
def _readjson(read):
    return json.load(read)

def _traceableurl(url):
    web = f'''https://is.gd/create.php?format=simple&logstats=1&url={url}'''
    resonse = requests.post(web)
    if(response.status_code!=200):
        print('ERROR:an error occurred during establishing a connection to the server')
        sys.exit()
    isgd = response.text
    return isgd

def _traceurl(url):
    web = 'http://is.gd/forward.php'
    params = { 'format': 'simple','shorturl': str(url) }
    headers = {'User-Agent': 'http://is.gd' }
    response = requests.get(web, params=params, headers=headers, verify=True)
    return response.text
   
def _removestring(data, remove):
    return data.replace(remove, '')
    
def _host(email, file):
    url = f'''https://drv.tw/~{email}/gd/QRlib/{file}'''
    res = requests.get(url)
    res = res.url
    return res
    
def _percentbar(data, qr):
    return tqdm(data,ncols=60,desc='QRlib',bar_format='{l_bar}{bar}| working on step {n_fmt} of {total_fmt} in %sQR'%(qr))
    
def _checknet():
	try:
		requests.get('https://mjfv74xauzaho1ipyjadzg-on.drv.tw/QRlib/net.txt').status_code
	except:
		print("You Are Not conected To Internet")
		print("QRlib Will Not Work Without Internet")
		sys.exit()
