from PIL import Image
'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型png, gif, jpeg...
'''
def ResizeImage(filein, fileout, width, height, type):
  img = Image.open(filein)
  out = img.resize((width, height),Image.ANTIALIAS) #resize image with high-quality
  out.save(fileout, type)
if __name__ == "__main__":
  filein = r'D:/Desktop/UAV_sunfall_i.jpg'
  fileout = r'D:/Desktop/UAV_sunfall_i_resize.jpg'
  width = 1920
  height = 1080
  type = 'PNG'
  ResizeImage(filein, fileout, width, height, type)