from cmath import sqrt
from PIL import Image
from pathlib import Path
from time import time
import math

def calcDistance(pix1, pix2):
    return (pix1[0]-pix2[0])**2 + (pix1[1]-pix2[1])**2 + (pix1[2]-pix2[2])**2

def countImgDistance(files, type):
    for file in files:
        img = Image.open(file)
        img.resize((500, 310))
        dis = 0
        for (pix1, pix2) in zip(testImg.getdata(), img.getdata()):
            dis += calcDistance(pix1, pix2)
        distance.append([math.sqrt(dis), type])

K = 3

start_time = time()

files1, files2 = Path('summer').glob('*'), Path('winter').glob('*')

testImg = Image.open('for-test.jpg')
testImg.resize((500, 310))

distance = list()

countImgDistance(files1, 'summer')
countImgDistance(files2, 'winter')

distance.sort(key = lambda x: x[0])

sc, wc = 0, 0
for i in range(K):
    if distance[i][1]=='summer': sc+=1
    else: wc+=1

if sc>wc: print('summer')
else: print('winter')
print("--- %s seconds ---" % (time() - start_time))