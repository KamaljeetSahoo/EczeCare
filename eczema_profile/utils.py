import cv2
from django.core.files.base import ContentFile
from pyowm.owm import OWM
import math

import torch, torchvision

import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection.mask_rcnn import MaskRCNNPredictor

      
def get_instance_segmentation_model(num_classes):
    # load an instance segmentation model pre-trained on COCO
    model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)

    # get the number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    # now get the number of input features for the mask classifier
    in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels
    hidden_layer = 256
    # and replace the mask predictor with a new one
    model.roi_heads.mask_predictor = MaskRCNNPredictor(in_features_mask,
                                                       hidden_layer,
                                                       num_classes)

    return model

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# our dataset has two classes only - background and person
num_classes = 2

# get the model using our helper function
model = get_instance_segmentation_model(num_classes)
# move model to the right device
model.to(device)


def poem_calc_score(d):
    score=0
    for i in range(1,8):
        score +=int( d['q'+str(i)][0])
    return score

def poem_calc_db(p):
    s = 0
    for i in range(1,8):
        s += getattr(p, 'q'+str(i))
    return s
def find_cor(temp_list,hum_list,p_list,p_total,t_total,h_total):
    p_avg = p_total/len(p_list)
    t_avg = t_total/len(temp_list)
    h_avg = h_total/len(hum_list)
    num=0
    num1=0
    den1 = 0
    num1 =0
    den2 = 0
    den3 =0
    r_t=0
    r_h=0
    for i in range(0,len(p_list)):
        num+=(p_list[i]-p_avg)*(temp_list[i]-t_avg)
        den1+=(p_list[i]-p_avg)*(p_list[i]-p_avg)
        den2+=(temp_list[i]-t_avg)*(temp_list[i]-t_avg)
        hum_list[i]=float(hum_list[i])
        print(type(h_avg),type(hum_list[i]))
        print(type(p_list[i]-p_avg),type(hum_list[i]-h_avg))
        num1+=(float(p_list[i]-p_avg))*(float(hum_list[i])-h_avg)
        
        den3+=(hum_list[i]-h_avg)*(hum_list[i]-h_avg)
    if den1*den2!=0:
        r_t = num/math.sqrt(den1*den2)
    if den1*den3!=0:
        r_h = num1/math.sqrt(den1*den3)
    return r_t,r_h
def last_severe(l):
    g = 1
    max = -1
    for i in range(1,8):
        sc = getattr(l,'q'+str(i))
        if sc>=g:
            g = sc
            max = i
    return max





def process_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret,th1 = cv2.threshold(image ,127,255, cv2.THRESH_BINARY)
    return th1

def encode_image(image):
    ret, buf = cv2.imencode('.jpg', image)
    content = ContentFile(buf.tobytes())
    return content

def weather():
    owm = OWM('744f0e49a7399e9cd187dd8544b364c4')
    mgr = owm.weather_manager()
    one_call = mgr.one_call(lat=52.5244, lon=13.4105)

    h = one_call.current.humidity # Eg.: 81
    temp = one_call.current.temperature()
    t = temp["temp"]
    return h,t

