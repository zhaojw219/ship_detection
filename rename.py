# -*- coding:utf8 -*-
import os

class BatchRename():
    def __init__(self):
        self.path='./image_path'
        
    def rename(self):
        filelist=os.listdir(self.path)  
        total_num=len(filelist)  
        i=1 
        for item in filelist:
            if item.endswith('.jpg'): 
                src=os.path.join(os.path.abspath(self.path),item)
                dst=os.path.join(os.path.abspath(self.path),''+str(i))
                #dst = os.path.join(os.path.abspath(self.path), '0000' + format(str(i), '0>3s') + '.jpg') 
                try:
                    os.rename(src,dst)
                    print('converting %s to %s ...' % (src, dst))
                    i=i+1
                except:
                    continue
        print('total %d to rename & converted %d jpgs' % (total_num, i))
        
if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
