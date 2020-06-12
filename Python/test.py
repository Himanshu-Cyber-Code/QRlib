#test.py

from QRlib.QRlib import *


qr.classic('data','classic')
print('')

qr.transparent('data','transparent')
print('')

qr.custom('data','custom')
print('')

qr.clear('data','clear')
print('')

qr.web(['data1','data2','data3'], 'web', tittle='tittle')
print('')

print(data.sms('+9192',message='message'))
print('')
print('')
print('')

print(data.text('text'))
print('')
print('')
print('')

print(data.url('https://google.com',short=True))
print('')
print('')
print('')

print(data.url('https://is.gd/'))
print('')
print('')
print('')

print(data.email('webstellarmouse@gmail.com',subject='subject',message='message'))
print('')
print('')
print('')

print(data.phone('+982'))
print('')
print('')
print('')

print(data.vcard2('name'))
print('')
print('')
print('')

print(data.vcard3('name'))
print('')
print('')
print('')

print(data.location(12345,12345))
print('')
print('')
print('')

print(data.wifi('ssid','password'))
print('')
print('')
print('')

print(data.event('tittle'))
print('')
print('')
print('')

print(data.mecard('name'))
print('')
print('')
print('')

print(data.host('webstellarmouse@gmail.com','net.txt'))
print('')
print('')
print('')
