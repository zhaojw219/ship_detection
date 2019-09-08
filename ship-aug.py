import base64
import json
from labelme import utils
import cv2 as cv
import sys
import numpy as np
import random
import re


class DataAugment(object):
    def __init__(self, image_id=1):
        # 盐噪声
        self.add_saltNoise = True
        # 高斯滤波
        self.gaussianBlur = True
        # 曝光度
        self.changeExposure = True
        # 随机裁剪
        # elf.randomcutImage = True
        self.id = image_id
        img = cv.imread(str(self.id)+'.png')  # 768x768 
        # img0 = cv.imread('img1.png')       # 1152x1152
        # img1 = cv.imread('img2.png')       # 1536x1536
        try:
            img.shape
        except:
            print('No Such image!---'+str(id)+'.png')
            sys.exit(0)
        self.src = img
        # self.src0 = img0
        # self.src1 = img1
        # cv.flip >0:沿x轴翻转 <0:x,y轴同时翻转 =0:沿y轴翻转
        dst1 = cv.flip(img, 0, dst=None)
        dst2 = cv.flip(img, 1, dst=None)
        dst3 = cv.flip(img, -1, dst=None)
        '''
        dst4 = cv.flip(img0, 0, dst=None)
        dst5 = cv.flip(img0, 1, dst=None)
        dst6 = cv.flip(img0, -1, dst=None)
        dst7 = cv.flip(img1, 0, dst=None)
        dst8 = cv.flip(img1, 1, dst=None)
        dst9 = cv.flip(img1, -1, dst=None)
        '''
        self.flip_x = dst1
        self.flip_y = dst2
        self.flip_x_y = dst3
        '''
        self.flip_x0 = dst4
        self.flip_y0 = dst5
        self.flip_x_y0 = dst6
        self.flip_x1 = dst7
        self.flip_y1 = dst8
        self.flip_x_y1 = dst9
        '''
        cv.imwrite(str(self.id)+'_flip_x'+'.png', self.flip_x)
        cv.imwrite(str(self.id)+'_flip_y'+'.png', self.flip_y)
        cv.imwrite(str(self.id)+'_flip_x_y'+'.png', self.flip_x_y)
        '''
        cv.imwrite(str(self.id)+'_flip_x0'+'.png', self.flip_x0)
        cv.imwrite(str(self.id)+'_flip_y0'+'.png', self.flip_y0)
        cv.imwrite(str(self.id)+'_flip_x_y0'+'.png', self.flip_x_y0)
        cv.imwrite(str(self.id)+'_flip_x1'+'.png', self.flip_x1)
        cv.imwrite(str(self.id)+'_flip_y1'+'.png', self.flip_y1)
        cv.imwrite(str(self.id)+'_flip_x_y1'+'.png', self.flip_x_y1)
        '''

    def gaussian_blur_fun(self):
        # 给原图、翻转后的图片加高斯噪声
        if self.gaussianBlur:
            dst1 = cv.GaussianBlur(self.src, (5, 5), 0)
            dst2 = cv.GaussianBlur(self.flip_x, (5, 5), 0)
            dst3 = cv.GaussianBlur(self.flip_y, (5, 5), 0)
            dst4 = cv.GaussianBlur(self.flip_x_y, (5, 5), 0)
            '''
            dst5 = cv.GaussianBlur(self.src0, (5, 5), 0)
            dst6 = cv.GaussianBlur(self.flip_x0, (5, 5), 0)
            dst7 = cv.GaussianBlur(self.flip_y0, (5, 5), 0)
            dst8 = cv.GaussianBlur(self.flip_x_y0, (5, 5), 0)

            dst9 = cv.GaussianBlur(self.src1, (5, 5), 0)
            dst10 = cv.GaussianBlur(self.flip_x1, (5, 5), 0)
            dst11 = cv.GaussianBlur(self.flip_y1, (5, 5), 0)
            dst12 = cv.GaussianBlur(self.flip_x_y1, (5, 5), 0)
            '''
            cv.imwrite(str(self.id)+'_Gaussian'+'.png', dst1)
            cv.imwrite(str(self.id)+'_flip_x'+'_Gaussian'+'.png', dst2)
            cv.imwrite(str(self.id)+'_flip_y'+'_Gaussian'+'.png', dst3)
            cv.imwrite(str(self.id)+'_flip_x_y'+'_Gaussian'+'.png', dst4)
            '''
            cv.imwrite(str(self.id)+'_Gaussian0'+'.png', dst5)
            cv.imwrite(str(self.id)+'_flip_x0'+'_Gaussian'+'.png', dst6)
            cv.imwrite(str(self.id)+'_flip_y0'+'_Gaussian'+'.png', dst7)
            cv.imwrite(str(self.id)+'_flip_x_y0'+'_Gaussian'+'.png', dst8)
            cv.imwrite(str(self.id)+'_Gaussian1'+'.png', dst9)
            cv.imwrite(str(self.id)+'_flip_x1'+'_Gaussian'+'.png', dst10)
            cv.imwrite(str(self.id)+'_flip_y1'+'_Gaussian'+'.png', dst11)
            cv.imwrite(str(self.id)+'_flip_x_y1'+'_Gaussian'+'.png', dst12)
            '''

    def change_exposure_fun(self):
        # 改变原图、翻转图曝光度，图片叠加
        if self.changeExposure:
            # contrast
            reduce = 0.5
            increase = 1.4
            # brightness
            g = 10
            h, w, ch = self.src.shape
            add = np.zeros([h, w, ch], self.src.dtype)
            # cv.addweighted(src1,alpha,src2,beta,0.0,dst)
            # 1、第1个参数，输入图片1， 
            # 2、第2个参数，图片1的融合比例
            # 3、第3个参数，输入图片2
            # 4、第4个参数，图片2的融合比例
            # 5、第5个参数，偏差
            # 6、第6个参数，输出图片
            dst1 = cv.addWeighted(self.src, reduce, add, 1-reduce, g)
            dst2 = cv.addWeighted(self.src, increase, add, 1-increase, g)
            dst3 = cv.addWeighted(self.flip_x, reduce, add, 1 - reduce, g)
            dst4 = cv.addWeighted(self.flip_x, increase, add, 1 - increase, g)
            '''
            dst5 = cv.addWeighted(self.flip_y, reduce, add, 1 - reduce, g)
            dst6 = cv.addWeighted(self.flip_y, increase, add, 1 - increase, g)
            dst7 = cv.addWeighted(self.flip_x_y, reduce, add, 1 - reduce, g)
            dst8 = cv.addWeighted(self.flip_x_y, increase, add, 1 - increase, g)
            '''
            cv.imwrite(str(self.id)+'_ReduceEp'+'.png', dst1)
            cv.imwrite(str(self.id)+'_flip_x'+'_ReduceEp'+'.png', dst3)
            # cv.imwrite(str(self.id)+'_flip_y'+'_ReduceEp'+'.png', dst5)
            # cv.imwrite(str(self.id)+'_flip_x_y'+'_ReduceEp'+'.png', dst7)
            cv.imwrite(str(self.id)+'_IncreaseEp'+'.png', dst2)
            cv.imwrite(str(self.id)+'_flip_x'+'_IncreaseEp'+'.png', dst4)
            # cv.imwrite(str(self.id)+'_flip_y'+'_IncreaseEp'+'.png', dst6)
            # cv.imwrite(str(self.id)+'_flip_x_y'+'_IncreaseEp'+'.png', dst8)

    def add_salt_noise(self):
        #　增加盐噪声
        if self.add_saltNoise:
            percentage = 0.005
            dst1 = self.src
            dst2 = self.flip_x
            dst3 = self.flip_y
            dst4 = self.flip_x_y

            num = int(percentage * self.src.shape[0] * self.src.shape[1])
            for i in range(num):
                rand_x = random.randint(0, self.src.shape[0] - 1)
                rand_y = random.randint(0, self.src.shape[1] - 1)
                if random.randint(0, 1) == 0:
                    dst1[rand_x, rand_y] = 0
                    dst2[rand_x, rand_y] = 0
                    dst3[rand_x, rand_y] = 0
                    dst4[rand_x, rand_y] = 0
                else:
                    dst1[rand_x, rand_y] = 255
                    dst2[rand_x, rand_y] = 255
                    dst3[rand_x, rand_y] = 255
                    dst4[rand_x, rand_y] = 255
            
            cv.imwrite(str(self.id)+'_Salt'+'.png', dst1)
            cv.imwrite(str(self.id)+'_flip_x'+'_Salt'+'.png', dst2)
            cv.imwrite(str(self.id)+'_flip_y'+'_Salt'+'.png', dst3)
            cv.imwrite(str(self.id)+'_flip_x_y'+'_Salt'+'.png', dst4)


    def json_generation(self):
        image_names = [str(self.id)+'_flip_x', str(self.id)+'_flip_y', str(self.id)+'_flip_x_y','0gogogo','1gogogo']
        if self.gaussianBlur:
            image_names.append(str(self.id)+'_Gaussian')
            image_names.append(str(self.id)+'_flip_x'+'_Gaussian')
            image_names.append(str(self.id)+'_flip_y' + '_Gaussian')
            image_names.append(str(self.id)+'_flip_x_y'+'_Gaussian')
    
        if self.add_saltNoise:
            image_names.append(str(self.id)+'_Salt')
            image_names.append(str(self.id)+'_flip_x' + '_Salt')
            image_names.append(str(self.id)+'_flip_y' + '_Salt')
            image_names.append(str(self.id)+'_flip_x_y' + '_Salt')
            
        for image_name in image_names:
            print(image_name)
            with open(str(self.id)+".json", 'r') as js:
                json_data = json.load(js)
                annotations = json_data['annotations']
                len_ann = len(annotations)
                ann = annotations[0]
                hei = ann.get('height')
                wid = ann.get('width')

                half_mask=[]
                final_mask=[]
                for an in annotations:
                    seg1 = an['segmentation']
                    print(seg1)
                    seg = seg1[0]
                    for j in range(0,len(seg),2):
                        match_pattern2 = re.compile(r'(.*)_x(.*)')
                        match_pattern3 = re.compile(r'(.*)_y(.*)')
                        match_pattern4 = re.compile(r'(.*)_x_y(.*)')
                        match_pattern5 = re.compile(r'img1')
                        match_pattern6 = re.compile(r'img2')
                        if match_pattern4.match(image_name):
                            seg[j] = wid - seg[j]
                            seg[j+1] = hei - seg[j+1]
                        elif match_pattern3.match(image_name):
                            seg[j] = wid - seg[j]
                            seg[j+1] = seg[j+1]
                        elif match_pattern2.match(image_name):
                            seg[j] = seg[j]
                            seg[j+1] = hei - seg[j+1]
                        elif match_pattern5.match(image_name):
                            seg[j] = 1.5*seg[j]
                            seg[j+1] = 1.5*seg[j+1]
                        elif match_pattern6.match(image_name):
                            seg[j] = 2*seg[j]
                            seg[j+1] = 2*seg[j+1]
                        else:
                            seg[j] = seg[j]
                            seg[j+1] = seg[j+1]
                images = json_data['images']
                img = images[0]
                img['file_name'] = str(image_name) + ".png"
                json.dump(json_data, open("./"+image_name+".json", 'w'), indent=4)
            
if __name__ == "__main__":
    ran = [0.5,2]
    print(ran)
    dataAugmentObject = DataAugment(1)
    # dataAugmentObject.random_resize_image(times=ran)
    dataAugmentObject.gaussian_blur_fun()
    dataAugmentObject.change_exposure_fun()
    dataAugmentObject.add_salt_noise()
    dataAugmentObject.json_generation()
    
