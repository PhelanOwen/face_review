import os
import face_recognition as fr
import pickle

dataset=[]

for img in [img for img in os.listdir('training') if '.jpg' in img]:
    dataset.append(fr.face_encodings(fr.load_image_file('training/' + img)))

f_d = open('face_data', 'wb')
pickle.dump(dataset, f_d)

f_d.close()