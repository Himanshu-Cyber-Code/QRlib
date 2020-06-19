import face_recognition
import pickle
import os
import numpy as np


def Train_Face_Match(img_folder_path, dat_file_output_path, delete=False, rename=False):
    os.getcwd()
    all_face_encodings = {}
    for i, filename in enumerate(os.listdir(img_folder_path)):
        tolal_file=i
    for i, filename in enumerate(os.listdir(img_folder_path)):
        print('TRAINING IMAGE  -  ',str(i+1),'/',tolal_file+1)
        i = str(i)
        if len(i)==1:
            i = "000"+i
        elif len(i)==2:
            i = "00"+i
        elif len(i)==3:
            i = "0"+i
        else:
            i = str(i)
        try:
            img = face_recognition.load_image_file(img_folder_path + filename)
            all_face_encodings[i] = face_recognition.face_encodings(img)[0]
            if rename:
                os.rename(img_folder_path + filename, img_folder_path + str(i) + ".jpg")
        except:
            print('NO FACE DETECTED IN IMAGE --  ',i )
            if delete:
                print('DELETING --  ',i )
                os.remove(img_folder_path + filename)
    with open(dat_file_output_path, 'wb') as f:
        pickle.dump(all_face_encodings, f)


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











Train_Face_Match('Face_data/testt/', 'bla-bla-bla.dat', delete=False, rename=False)






