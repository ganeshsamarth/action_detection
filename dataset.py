import pandas as pd
import random
import os
import cv2
video_directory='/home/pbu/ActivityNet/Crawler/Kinetics/youtube_videos'
data=pd.read_csv('/home/pbu/Downloads/kinetics_train/kinetics_train.csv')
labels_list=data['label']
youtube_id_list=data['youtube_id']
num_examples=len(youtube_id_list)
num_videos=200
num_frames_per_video=40
label_names=os.listdir(video_directory)

for i,labels in enumerate(label_names):
    for videos in random.sample(os.listdir(video_directory+'/'+labels),num_videos):
        vidcap = cv2.VideoCapture(videos)
        frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        jump_frame=frame_count//num_frames_per_video
        success, image = vidcap.read()
        count = 0
        os.mkdir(video_directory+'/'+labels+'/'+videos)
        while success:
            if count%jump_frame==0:
                cv2.imwrite("frame%d.jpg" % count, image)  # save frame as JPEG file
                success, image = vidcap.read()
                print('Read a new frame: ', success)
            count += 1

