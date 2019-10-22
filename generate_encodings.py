import os
import face_recognition as fr
import pickle
import random
import numpy as np

dataset=[]

for r in os.listdir('training'):
    for img in [img for img in os.listdir('training/' + r) if '.jpg' in img]:
        dataset.append([fr.face_encodings(fr.load_image_file('training/' + r + '/' + img))[0], int(r)])

print (len(dataset))

random.shuffle(dataset)

x = []
y = []

for features, label in dataset:
    x.append(features)
    y.append(label)

x = np.array(x)

f_d = open('x.face_data', 'wb')
pickle.dump(x, f_d)
f_d.close()

f_d = open('y.face_data', 'wb')
pickle.dump(y, f_d)
f_d.close()