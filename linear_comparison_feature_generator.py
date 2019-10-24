print ("Uh oh, here we go...")

import face_recognition as fr
import os, time, pickle, random
import numpy as np

number_of_faces_to_test_against = 15
average_face = {}

for r in os.listdir('training'):
    # r here being 0-5
    print("Training faces for rating:",r)

    file_list = [img for img in os.listdir('training/' + r) if '.jpg' in img]

    # if there's less faces than needed, just don't bother
    # if (len(file_list) < number_of_faces_to_test_against):
    #     print("You need more faces with a rank of", r, "- You are", number_of_faces_to_test_against-int(r),"short!")
    #     time.sleep(3)
    #     exit(0)

    iter_n = int(len(file_list) / number_of_faces_to_test_against)

    if iter_n == 0:
        iter_n = 1

    file_chunk = [file_list[i:i+iter_n] for i in range(0, len(file_list), iter_n)]

    # Now we have number_of_faces_to_test_against bunches of faces to average out
    for ind, chunk in enumerate(file_chunk):
        print(ind+1, "/", len(file_chunk))

        # this first entry of zeros will be ignored
        face = np.zeros(128)
        for img in chunk:
            face += fr.face_encodings(fr.load_image_file('training/' + r + '/' + img))[0]

        face /= len(chunk)
        try:
            average_face[r].append(face)
        except:
            average_face[r] = [face]

pickle.dump(average_face, open('LinearEstimatorData.dat', 'wb'))
print("Complete! Press enter to close...")
ex = input()