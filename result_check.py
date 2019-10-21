import os

files = [f for f in os.listdir('.') if '.txt' in f]

scores = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0}

for f in files:
    key = open(f).read()
    scores[key] += 1

for (k,v) in scores.items():
    print(k, v)
print ( "Total:", len(files) )