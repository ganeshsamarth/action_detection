import os
import numpy as np
import cv2
video_directory='/home/pbu/ActivityNet/Crawler/Kinetics/youtube_videos'
label_names=os.listdir(video_directory)
train_X=np.empty(0,224,224,3)
for i,labels in enumerate(label_names):

    video_names=os.listdir(video_directory+'/'+labels)
    for videos in video_names:
        images=os.listdir(video_directory+'/'+labels+'/'+videos)
        for image in images:
            img=cv2.imread(video_directory+'/'+labels+'/'+videos+'/'+image)
            img=img/255 #normalize data
            train_X=np.append(train_X,img,axis=0)




