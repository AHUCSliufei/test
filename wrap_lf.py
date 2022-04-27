from posixpath import join
import cv2 as cv
import numpy as np
import os
import json
import math
import csv
from skimage.measure import compare_ssim as ssim
from PIL import Image
import random

# ta means time align
exp_path = '/DATA/yangmengmeng/liufei/DeepHomography-master/Sequence/fastwhite/'
# new wrap img save path
wrap_save_path = exp_path+'allin_point48_wrap_i_ta_lowsolu/'
# load points from json file
json_file_path_v = join(exp_path,'v000_Label_point48_ta_lowsolu.json')
json_file_path_i = join(exp_path,'i000_Label_point48_ta_lowsolu.json')


#select two images to draw random point  
point_image_path_v = join(exp_path,'visible/v000.jpg')
point_image_path_i = join(exp_path,'all_point80_wrap_i_ta/i000.jpg')
#save two images which have drawed random point 
save_draw_point_img_path_v = join(exp_path,'draw_point_v80_ta.jpg')
save_draw_point_img_path_i = join(exp_path,'draw_point_i80_ta.jpg')


img_list = os.listdir(exp_path+'visible')
a = 000
b = len(img_list)

def point(json_file_path):
    with open(json_file_path, 'r') as f:
        temp = json.loads(f.read())
        target=temp['Models']['LandMarkListModel']['Points'][0]
        targetList=target['LabelList']
        targetList.sort(key=lambda k: (k.get('Label', 0)))
        positionlist=[]
        
        for i in targetList:
            temp=i['Position'][0:2]
            temp[0]=math.ceil(temp[0])
            temp[1]=math.ceil(temp[1])
            positionlist.append(temp)
            
        f = open('Position.csv','w',newline='')
        writer = csv.writer(f)
        for i in positionlist:
            writer.writerow(i)
        f.close()
    
    f = csv.reader(open('Position.csv','r'))
    show=[]
    for i in f:
        i[0]=int(i[0])
        i[1]=int(i[1])
        show.append(i)
    return show

def wrap(exp_path,json_file_path_v,json_file_path_i,wrap_save_path):

    for order in range(a,b):
        order = "{:0>3}".format(order)
        original_image = cv.imread(exp_path+'infrared/'+'i%s'%order+'.jpg')
        #print(exp_path+'infrared/'+'v%s'%order+'.jpg')
        target_image = cv.imread(exp_path+'visible/'+'v%s'%order+'.jpg')

        #print(exp_path+'visible/'+'v%s'%order+'.jpg')
        den_more_v_point= np.float32(
            point(json_file_path_v)
            ).reshape(-1, 1, 2)

        src_more_i_point= np.float32(
            point(json_file_path_i)
            ).reshape(-1, 1, 2)

        
        #H, status = cv.findHomography(src_more_i_point, den_more_v_point, cv.RANSAC, 6.0)
        H, status = cv.findHomography(src_more_i_point, den_more_v_point, 0)
        warped_more_point_image = cv.warpPerspective(original_image, H, (target_image.shape[1], target_image.shape[0]))

        if not os.path.exists(wrap_save_path):
            os.makedirs(wrap_save_path)
        cv.imwrite(wrap_save_path+'i'+'%s'%order+'.jpg',warped_more_point_image)
        print('image%s'%order)    
    
    return H

def count_ssim(target_image,original_image,save_path,order):

    new_image_i = cv.imread(save_path+'i'+'%s'%order+'.jpg')
    crop_new_image_i = new_image_i[150:930,200:1720]#y0:y1,x0:x1
    crop_target_image = target_image[150:930,200:1720]
    crop_image_i = original_image[150:930,200:1720]
    compare_new_i = cv.cvtColor(crop_new_image_i, cv.COLOR_BGR2GRAY)
    compare_i = cv.cvtColor(crop_image_i, cv.COLOR_BGR2GRAY)
    compare_v = cv.cvtColor(crop_target_image, cv.COLOR_BGR2GRAY)
    ssim_value_newi2v = ssim(compare_new_i,compare_v)
    ssim_value_orgi2v = ssim(compare_i,compare_v)
    print('the value of new_i and v ssim is   ',ssim_value_newi2v)
    print('the value of org_i and v ssim is   ',ssim_value_orgi2v)


def draw_rand_point(path_image_v,path_image_new_i,save_path_i,save_path_v):

    image_v = Image.open(path_image_v)
    image_new_i = Image.open(path_image_new_i)

    width = 1920
    height = 1080

    for w in range(1,15):
        w = w *128-random.randint(1,100)
        for h in range(1,8):
            h = h*135-random.randint(1,134)
            r = random.randint(1,30)
            for i in range(w-r-10,w-r):
                for j in range(h+r-10,h+r):
                    image_v.putpixel((i,j), (0, 255, 0))
                    image_new_i.putpixel((i,j), (0, 255, 0)) 
    
    image_v.save(save_path_i)
    image_new_i.save(save_path_v)



if __name__=="__main__":
    H = wrap(exp_path,json_file_path_v,json_file_path_i,wrap_save_path)
    print(H)
    #draw_rand_point(point_image_path_v,point_image_path_i,save_draw_point_img_path_i,save_draw_point_img_path_v)
    print('success to draw points')





