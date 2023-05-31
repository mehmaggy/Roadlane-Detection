import os
import re
import cv2
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from os.path import isfile, join
col_frames=os.listdir('frames/') 
#load frames
col_images = []
for i in tqdm(col_frames):
    img = cv2.imread('frames/'+ i)
    col_images.append(img)
#specific frame
idx = 457
stencil=np.zeros_like(col_images[idx][:,:,0])
#Specify coordinates of the polygon
polygon=np.array([[50,270],[220,160],[360,160],[480,270]])
#fil polygon 
cv2.fillConvexPoly(stencil,polygon,1)
img=cv2.bitwise_and(col_images[idx][:,:,0],col_images[idx][:,:,0],mask=stencil)
ret,thresh=cv2.threshold(img,130,145,cv2.THRESH_BINARY)
lines=cv2.HoughLinesP(thresh,1,np.pi/180,30,maxLineGap=200)
#Create a copy of the origninal frame
dmy=col_images[idx][:,:,0].copy()
#draw houghlines
for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(dmy,(x1,y1),(x2,y2),(255,0,0),3)
#plot frame
plt.figure(figsize=(10,10))
plt.imshow(dmy,cmap="gray")
plt.show()