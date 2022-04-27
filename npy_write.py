from posixpath import join
import numpy as np
import os

# ta means time align
exp_path = '/DATA/yangmengmeng/liufei/DeepHomography-master/Data/'
video_path = exp_path +'UAV_Test/visible/'
npy_save_path = os.path.join(exp_path,'UAV_Coordinate')

def npysave(npy_save_path):
    video_list = os.listdir(video_path)
    for video_name in video_list:
        img_path = os.path.join(video_path,video_name)
        txt1_path = os.path.join(exp_path,video_name,'.txt')
        txt2_path = os.path.join(exp_path,video_name.replace('v','i'),'.txt')        
        img_list = os.listdir(img_path)
        for img_name in img_list:
            img1_name = img_name
            img2_name = img1_name.replace('v','i')
            dic = {'path1':img1_name,'path2':img2_name,'matche_pts':[]}
            i = 0
            for line1,line2 in open(txt1_path,txt2_path):  
                dic['matche_pts'][i] = [line1,line2]
                i = i+1
            if not os.path.exists(npy_save_path):
                os.makedirs(npy_save_path)
            np.save(os.path.join(npy_save_path,img1_name,'_',img2_name,'.npy'),dic)


if __name__=="__main__":

    npysave(npy_save_path)
    print('success to svae npyfile')





