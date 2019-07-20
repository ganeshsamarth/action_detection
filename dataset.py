import pandas as pd
import random
import os
import cv2
video_directory='/home/pbu/ActivityNet/Crawler/Kinetics/youtube_videos'
data=pd.read_csv('/home/pbu/Downloads/kinetics_train/kinetics_train.csv')
#data=pd.read_csv('C:\\Users\\ganeshsamarth\\Downloads\\kinetics_train.csv')
labels_list=data['label']
labels_list_no_space=list()
youtube_id_list=data['youtube_id']
num_examples=len(youtube_id_list)
num_videos=200
num_frames_per_video=40
label_names=os.listdir(video_directory)
for labels in labels_names:
    labels_list_no_space.append(labels.replace(" ",""))
    os.rename(video_directory+'/'+labels,video_directory+'/'+labels.replace(" ",""))
#print(labels_list_no_space)





'''
for i,labels in enumerate(labels_list_no_space):
    for videos in random.sample(os.listdir(video_directory+'/'+labels),num_videos):
        vidcap = cv2.VideoCapture(videos)
        frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        jump_frame=frame_count//num_frames_per_video
        success, image = vidcap.read()
        count = 0
        os.mkdir(video_directory+'/'+labels+'/'+videos)
        while success:
            if count%jump_frame==0:
                cv2.imwrite(video_directory+'/'+labels+'/'+videos+'/'+"frame%d.jpg" % count, image)  # save frame as JPEG file
            success, image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1
'''
