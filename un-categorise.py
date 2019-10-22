import shutil
import os

for root, dirs, files in os.walk('training'):
    for f in files:
        shutil.move(os.path.join(root, f), f)


for root, dirs, files in os.walk('validation'):
    for f in files:
        shutil.move(os.path.join(root, f), f)

for root, dirs, files in os.walk('score_info'):
    for f in files:
        shutil.move(os.path.join(root, f), f)