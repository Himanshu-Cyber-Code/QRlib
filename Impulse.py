print('http://192.168.43.136:5000/FR?face=')


import base64
import face_recognition
import pickle
import os
import numpy as np



def base2img(base64):
    imgdata = base64.b64decode(sys.argv[1])
    with open('CURRENT_IMAGE.png', 'wb') as f:
        f.write(imgdata)

def Match_Face(img_path, dat_path, face_tolerance, total_encoding):
    face_match_percentage = 0
    face_match_number = 0

    with open(dat_path, 'rb') as f:
    	    all_face_encodings = pickle.load(f)
	
    face_names = list(all_face_encodings.keys())
    face_encodings = np.array(list(all_face_encodings.values()))

    unknown_image = face_recognition.load_image_file(img_path)
    unknown_face = face_recognition.face_encodings(unknown_image)

    face_match_result = face_recognition.compare_faces(face_encodings, unknown_face,tolerance=face_tolerance)
    result = list(zip(face_names, face_match_result))

    for i in range(total_encoding+1):
        if result[i][1]:
            num = 1
        else:
            num = 0
        face_match_number = num + face_match_number

    face_match_percentage = (face_match_number / (total_encoding))*100

    return face_match_percentage

import flask
from flask import request, jsonify
app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '''<html><body bgcolor="blue"><h1>Face Recognition</h1</body></html>'''
    
@app.route('/FR', methods=['GET'])
def api_data():
    if 'face' not in request.args:
        return '''<html><body bgcolor="blue"><h1>PROVIDE SOME DATA</h1></body></html>'''
    if 'face' in request.args:
        base2img(request.args['face'])
        did=Match_Face('CURRENT_IMAGE.png', 'Himanshu-Face-Encodings.dat', 0.5, 349)
        

    else:
        return """<html><body bgcolor="red"><b><h1>Data Sending Process Failed</h1></b></body></html>"""
        
    return did
    
app.run(host="192.168.43.136")
