import gluoncv
from gluoncv import model_zoo, data, utils
from collections import defaultdict
import json
from flask import Flask,Response,request
from flask import send_file
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

# net = model_zoo.get_model('ssd_512_resnet50_v1_voc', pretrained=True)
net = model_zoo.get_model('faster_rcnn_resnet50_v1b_voc', pretrained=True)
#net = model_zoo.get_model('yolo3_darknet53_voc', pretrained=True)
# @app.route('/',methods = ['GET','POST','OPTIONS'])
# def hello():
# 	ans = {"msg":"This is it"}
# 	json_ans = json.dumps(ans, sort_keys=True)
# 	return Response(json_ans)
@app.route('/getImageDetails',methods = ['GET','POST'])
def calculate():
	try:
		if request.method == 'POST':
			story = request.files.get('file')
			image = story.save('filename.png')
			# x, img = data.transforms.presets.ssd.load_test('filename.png',short = 512)
			x, img = data.transforms.presets.rcnn.load_test('filename.png',short = 512)
			# x, img = data.transforms.presets.yolo.load_test('filename.png',short = 512)

			box_ids, scores, bboxes = net(x)
			# print(net.classes)
			n_box = box_ids.shape[1]
			ans = defaultdict(int)
			for n in range(n_box):
				if box_ids[0][n].asscalar() != -1:
					if float(scores[0][n].asscalar()) > 0.5:
						ans[net.classes[int(box_ids[0][n].asscalar())]] += 1
			ax = utils.viz.plot_bbox(img, bboxes[0], scores[0],
                         box_ids[0], class_names=net.classes)
		
		else:
			ans = {"Message":"Get method is not allowed. Post an image for object detection."}
	except(Exception):
			ans = {"Message":"Some exception occured"}

	
	json_ans = json.dumps(ans, sort_keys=True)

	
	return(json_ans)

if __name__ == '__main__':
	app.run()