from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def histSimiliar(lh,rh):
    assert len(lh)==len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r))/max(l, r)) for l, r in zip(lh, rh))/len(lh)
def splitImg(img,partSize):
    w,h=img.size
    pw,ph=partSize
    returnValue=[img.crop((i,j,i+pw,j+ph)).copy() for i in range(0,w,pw) for j in range(0,h,ph)]
    return returnValue
def calculate(li,ri,widthSplit,heightSplit):
    partSize=int(li.size[0]/widthSplit),int(ri.size[1]/heightSplit)
    return sum(histSimiliar(l.histogram(), r.histogram()) for l, r in zip(splitImg(li,partSize), splitImg(ri,partSize))) / (widthSplit*heightSplit)
source=Image.open('F:\git\PythonStudy\ImageCompare\Original.png').convert('L')
changed=Image.open('F:\git\PythonStudy\ImageCompare\Changed2.png').convert('L')
'''sourceHistogram=source.convert('L').resize((1024,1024)).histogram()
changedHistogram=changed.convert('L').resize((1024,1024)).histogram()

plt.plot(sourceHistogram)
plt.plot(changedHistogram)'''
print(source.size)
print(calculate(source,changed,1,1))
plt.show()
pass
