import h5py
f = h5py.File('/media/gnss/系统/zhaojw/Mask_RCNN-master_coco/mask_rcnn_coco.h5','r')
for key in f.keys():
	print(f[key].name)
	print(f[key])
