import pandas as pd
import os
import numpy as np
import csv
import shutil

file_read = open("./train_ship_segmentations_v2.csv", "r")
reader = csv.reader(file_read)

fileHeader = ["ImageId", "EncodedPixels"] # 建立表头
file_write = open("./positive.csv", "w")
writer = csv.writer(file_write)
writer.writerow(fileHeader)

positive_example_dic = {}

# 生成保存 positive examples 信息的 csv
for item in reader:
    if reader.line_num == 1: # 忽略第一行表头
        continue
    else:
        if item[1] != '':
            writer.writerow(item) 
            positive_example_dic[item[0]] = item[1] # 生成保存 positive examples 图片名的字典，不用列表，因为字典查找更快

file_read.close()
print('csv done!')

'''
# 把 postive examples 移动到一个文件夹
original_sample_path = '/media/gnss/系统/zhaojw/file:/home/gnss/NewDisk/zhaojw/competitions/airbus-ship-detection/train_v2'
positive_sample_path = '/home/gnss/Desktop/all_positive_images'
file_set = os.listdir(original_sample_path)
count = 0 # 记录positive example个数

for i in file_set:
    if i in positive_example_dic:
        example = os.path.join(original_sample_path,i)
        count += 1

        shutil.copy(example, positive_sample_path)

print('copy positive samples successfully, there are '+ str(count)+' postive examples!')
'''
