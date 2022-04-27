import os

v_path = "/DATA/yangmengmeng/liufei/DeepHomography-master/Data/UAV_Test/visible"
i_path = "/DATA/yangmengmeng/liufei/DeepHomography-master/Data/UAV_Test/infrared"
def list_order(v_path, i_path):
    v_file = os.listdir(v_path)
    v_file.sort()
    i_file = os.listdir(i_path)

    i_file.sort()
    f_open = open('/DATA/yangmengmeng/liufei/DeepHomography-master/Data/test_UAVTest_List.txt','w')

    for v_name,i_name in zip(v_file,i_file):
        v_image_path = os.path.join(v_path,v_name)
        v_image_list = os.listdir(v_image_path)
        v_image_list.sort()
        i_image_path = os.path.join(i_path,i_name)
        i_image_list = os.listdir(i_image_path)
        i_image_list.sort()
        for v_image,i_image in zip(v_image_list,i_image_list):
            v_image_line = os.path.join(v_name,v_image)
            i_image_line = os.path.join(i_name,i_image)
            f_open.writelines(v_image_line+" "+i_image_line+"\n")

if __name__=="__main__":
    
    list_order(v_path, i_path)
    print("success")