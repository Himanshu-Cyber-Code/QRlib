from . import _util as ql

def text(qrdata):
    ql._checkdata(qrdata, 'string', 'TEXT DATA FOR QR')
    return str(qrdata)
    
def url(qrdata, short=False):
    ql._checkdata(qrdata, 'string', 'URL DATA FOR QR')
    ql._checkdata(short, False, 'URL SHORTNING OPTION')
    if(short):
        return ('URL:'+str(ql._shorturl(qrdata)))
    else:
        return ('URL:'+str(qrdata))
        
def email(email, subject='', message=''):
    ql._checkdata(email, 'string', 'EMAIL DATA FOR QR')
    ql._checkdata(subject, 'string', 'SUBJECT DATA FOR QR')
    ql._checkdata(message, 'string', 'MESSAGE DATA FOR QR')
    ql._verifyemail(str(email))
    return f'''mailto:{email}?subject={subject}&body={message}'''
    
def phone(qrdata):
    ql._checkdata(qrdata, 'string', 'PHONE DATA FOR QR')
    return f'''tel:{qrdata}'''
    
def sms(phone, message=''):
    ql._checkdata(phone, 'string', 'PHONE DATA FOR QR')
    ql._checkdata(message, 'string', 'MESSAGE DATA FOR QR')
    return f'''SMSTO:{phone}:{message}'''
    
def vcard2(firstname, lastname='', position='', work='', org='', website='', email='', phone='', homephone='', workphone='', homefax='', workfax='', city='', state='', country='', zipcode='', street=''):
    ql._checkdata(firstname, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(lastname, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(position, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(work, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(org, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(website, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(email, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(phone, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(homephone, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(workphone, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(homefax, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(workfax, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(city, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(state, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(country, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(zipcode, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(street, 'string', 'VCARD2 DATA FOR QR')
    vcard2=f'''BEGIN:VCARD
VERSION:2.1
N:{lastname};{firstname}
TITLE:{position} {work}
ORG:{org}
URL:{website}
EMAIL;TYPE=INTERNET:{email}
TEL;CELL:{phone}
TEL;WORK;VOICE:{workphone}
TEL;HOME;VOICE:{homephone}
TEL;WORK;FAX:{workfax}
TEL;HOME;FAX:{homefax}
ADR:;;{street};{city};{state};{zipcode};{country}
END:VCARD'''
    return vcard2
    
def vcard3(firstname, lastname='', position='', work='', org='', website='', email='', phone='', homephone='', workphone='', homefax='', workfax='', city='', state='', country='', zipcode='', street=''):
    ql._checkdata(firstname, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(lastname, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(position, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(work, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(org, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(website, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(email, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(phone, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(homephone, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(workphone, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(homefax, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(workfax, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(city, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(state, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(country, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(zipcode, 'string', 'VCARD2 DATA FOR QR')
    ql._checkdata(street, 'string', 'VCARD2 DATA FOR QR')
    vcard3=f'''BEGIN:VCARD
VERSION:3.0
N:{lastname};{firstname}
FN:{firstname} {lastname}
TITLE:{position} {work}
ORG:{org}
URL:{website}
EMAIL;TYPE=INTERNET:{email}
TEL;TYPE=voice,work,pref:1
TEL;TYPE=voice,home,pref:2
TEL;TYPE=voice,cell,pref:{phone}
TEL;TYPE=fax,work,pref:4
TEL;TYPE=fax,home,pref:5
ADR:;;{street};{city};{state};{zipcode};{country}
END:VCARD'''
    return vcard3
    
def location(Latitude, Longitude):
    ql._checkdata(Latitude, 0, 'LATITUDE FOR QR', _less=0)
    ql._checkdata(Longitude, 0, 'LONGITUFE FOR QR', _less=0)
    url=f'''https://maps.google.com/local?q={float(Latitude)},{float(Longitude)}'''
    web=ql._shorturl(url)
    return str(web)
    
def wifi(ssid, password, encryption=0):
    ql._checkdata(ssid, 'string', 'SSID FOR QR')
    ql._checkdata(password, 'string', 'PASSWORD FOR QR')
    ql._checkdata(encryption, 0, 'ENCRYPTION FOR QR',_more=2)
    enc={'0':'nopass','1':'WPA','2':'WEP'}
    wifi=f'''WIFI:S:{ssid};T:{enc[str(encryption)]};P:{password};;'''
    return wifi
    
def event(tittle, location='',start=ql._nowtimedate(), end=ql._nowtimedate()):
    ql._checkdata(tittle, 'string', 'TITTLE FOR QR')
    ql._checkdata(location, 'string', 'LOCATION FOR QR')
    ql._checkdata(start, ['Q','R'], 'START TIME AND DATE FOR QR')
    ql._checkdata(end, ['Q','R'], 'END TIME AND DATE FOR QR')
    ql._checkdata(start[0], 0, 'YEAR DATA IN START FIELD OF EVENT')
    ql._checkdata(start[1], 0, 'MONTH DATA IN START FIELD OF EVENT', _more=12, _less=0)
    ql._checkdata(start[2], 0, 'DATE DATA IN START FIELD OF EVENT', _more=31, _less=0)
    ql._checkdata(start[3], 0, 'HOUR DATA IN START FIELD OF EVENT', _more=24, _less=0)
    ql._checkdata(start[4], 0, 'MINUTE DATA IN START FIELD OF EVENT', _more=60, _less=0)
    ql._checkdata(end[0], 0, 'YEAR DATA IN END FIELD OF EVENT')
    ql._checkdata(end[1], 0, 'MONTH DATA IN END FIELD OF EVENT', _more=12, _less=0)
    ql._checkdata(end[2], 0, 'DATE DATA IN END FIELD OF EVENT', _more=31, _less=0)
    ql._checkdata(end[3], 0, 'HOUR DATA IN END FIELD OF EVENT', _more=24, _less=0)
    ql._checkdata(end[4], 0, 'MINUTE DATA IN END FIELD OF EVENT', _more=60, _less=0)
    if(len(str(start[1]))==1):
        sm='0'+str(start[1])
    else:
        sm=str(start[1])
    if(len(str(start[2]))==1):
        sd='0'+str(start[2])
    else:
        sd=str(start[2])
    if(len(str(start[3]))==1):
        sh='0'+str(start[3])
    else:
        sh=str(start[3])
    if(len(str(start[4]))==1):
        smi='0'+str(start[4])
    else:
        smi=str(start[4])
    if(len(str(end[1]))==1):
        em='0'+str(end[1])
    else:
        em=str(end[1])
    if(len(str(end[2]))==1):
        ed='0'+str(end[2])
    else:
        ed=str(end[2])
    if(len(str(end[3]))==1):
        eh='0'+str(end[3])
    else:
        eh=str(end[3])
    if(len(str(end[4]))==1):
        emi='0'+str(end[4])
    else:
        emi=str(end[4])
    sy=str(start[0])
    ey=str(end[0])
    event=f'''BEGIN:VEVENT
SUMMARY:{tittle}
LOCATION:{location}
DTSTART:{sy}{sm}{sd}T{sh}{smi}00
DTEND:{ey}{em}{ed}T{eh}{emi}00
END:VEVENT'''
    return event
    
def mecard(firstname, lastname='', nickname='', email='', phone1='', phone2='', phone3='', dob=ql._nowtimedate(), note='', city='', state='', country='', zipcode='', street=''):
    ql._checkdata(firstname, 'string', 'MECARD DATA FOR QR')
    ql._checkdata(lastname, 'string', 'MECARD DATA FOR QR')
    ql._checkdata(nickname, 'string', 'MECARD DATA FOR QR')
    ql._checkdata(city, 'string', 'MECARD DATA FOR QR')
    ql._checkdata(state, 'string', 'MECARD DATA FOR QR')
    ql._checkdata(country, 'string', 'MECARD DATA FOR QR')
    ql._checkdata(zipcode, 'string', 'MECARD DATA FOR QR')
    ql._checkdata(street, 'string', 'MECARD DATA FOR QR')
    ql._checkdata(email, 'string', 'MECARD DATA FOR QR')
    ql._checkdata(phone1, 'string', 'MECARD DATA FOR QR')
    ql._checkdata(phone3, 'string', 'MECARD DATA FOR QR')
    ql._checkdata(phone3, 'string', 'MECARD DATA FOR QR')
    ql._checkdata(note, 'string', 'MECARD DATA FOR QR')
    ql._checkdata(dob, ['Q','R'], 'MECARD DATA FOR QR')
    ql._checkdata(dob[0], 0, 'MECARD DATA FOR QR')
    ql._checkdata(dob[1], 0, 'MECARD DATA FOR QR')
    ql._checkdata(dob[2], 0, 'MECARD DATA FOR QR')
    return f'''MECARD:N:{lastname},{firstname};NICKNAME:{nickname};TEL:{phone1};TEL:{phone2};TEL:{phone3};EMAIL:{email};BDAY:{dob[0]}/{dob[1]}/{dob[2]};NOTE:{note};ADR:,,{street},{city},{state},{zipcode},{country};;'''
    
def host(email, file):
    ql._checkdata(email, 'string', 'EMAIL DATA FOR QR')
    ql._checkdata(file, 'string', 'FILE NAME DATA FOR QR')
    ql._verifyemail(str(email))
    url = ql._host(email,file)
    host = 'URL:'+str(ql._shorturl(url))
    return host
    
def trace(urlweb,url=1):
    ql._checkdata(urlweb, 'string', 'URL FOR SITE DATA FOR QR')
    ql._checkdata(file, 0, 'URL TYPE DATA FOR QR',_more=1,_less=0)
    url = 'URL:'+str(ql._traceableurl(urlweb))
    urldata = ql._geturldata(urlweb)
    if(url==1):
        return url
    if(url==0):
        return ql._shorturl(str("https://"+urldata))


    
    
    
    
    
    
    
 
        
        
        
        
        
        
        