import shutil

files = [f for f in shutil.os.listdir('.') if '.jpg' in f]

try:
    shutil.os.mkdir('training')
    shutil.os.mkdir('validation')
    shutil.os.mkdir('score_info')

except:
    pass

try:
    for i in range(0,6):
        shutil.os.mkdir('training/' + str(i))
        shutil.os.mkdir('validation/' + str(i))
except:
    pass

for i,f in enumerate(files):
    res = 'r' + f[1:-3] + 'txt'
    score = open(res, 'r').read()

    if i%9 == 0:
        shutil.move(f, 'validation/'+str(score) +'/' + f)
    else:
        shutil.move(f, 'training/'+str(score) +'/' + f)

    shutil.move(res, 'score_info/'+res)