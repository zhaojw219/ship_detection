import json
import os

with open("1.json",'r') as orijson:
	# 打开原图的json，后续往这里面添加新属性
	original_json = json.load(orijson)
	images = original_json['images']
	annotations = original_json['annotations']
	img = images[0]
	length = len(annotations)
	print(type(images))
	print(type(img))

	a = 2

	json_file = './json_Folder'
	for file in os.listdir(json_file):
		if os.path.splitext(file)[1] == '.json':
			with open('./json_Folder/{}'.format(file),'r') as addjson:
				print(addjson)
				add_json = json.load(addjson)
				addimages = add_json['images']
				addannotations = add_json['annotations']
				add_length = len(addannotations)
				add_json['images'][0].update({'id':a})
				print(annotations)
				for i in range(1,add_length+1):
					print(i)
					print(add_json['annotations'][i-1])
					add_json['annotations'][i-1].update({'id':i+length}) # 修改待加入json中annotation里面的id为自加
					add_json['annotations'][i-1].update({'image_id':a})
					annotations.append(add_json['annotations'][i-1])
				print(annotations)
				new_length = len(annotations)
				print(new_length)
				length = new_length
				a += 1
		#print(add_json['annotations'])
			images.append(add_json['images'][0])
			json.dump(original_json,open("newcomplete.json",'w'),indent=4)
