import pickle, os
import face_recognition as fr

face_data = pickle.load(open('LinearEstimatorData.dat', 'rb'))

# TODO: add option to rate specific image

# os.mkdir('ai_guesses')
# for i in range(0,6):
#     os.mkdir('ai_guesses/'+str(i))

def find_rating(f_enc):
    closest_match = 0.0
    closest_rating = 0

    for r in face_data.keys():
        face_list = face_data[r]
        for face in face_list:
            match = 0.0
            match = fr.face_distance(f_enc, face)
            # print(match, r)
            if match > closest_match:
                closest_match = match
                closest_rating = r
    return closest_match, closest_rating


for rating in os.listdir('validation'):
    for img in os.listdir('validation/' + str(rating)):
        im_name = 'validation/' + str(rating) + '/' + img
        image = fr.load_image_file(im_name)
        face_encoding = fr.face_encodings(image)

        percent, guess_rating = find_rating(face_encoding)
        print(percent, guess_rating, im_name)
        # exit(0)



