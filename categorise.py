import shutil

files = [f for f in shutil.os.listdir('.') if '.jpg' in f]

try:
    shutil.os.mkdir('training')
    shutil.os.mkdir('validation')
except:
    pass

for i,f in enumerate(files):
    res = 'r' + f[1:-3] + 'txt'
    if i%2 == 0:
        shutil.move(f, 'training/'+f)
        shutil.move(res, 'training/'+res)
    else:
        shutil.move(f, 'validation/'+f)
        shutil.move(res, 'validation/'+res)