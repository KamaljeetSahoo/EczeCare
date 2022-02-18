import cv2
from django.core.files.base import ContentFile
from pyowm.owm import OWM
import math
from PIL import Image
import numpy as np
import torch, torchvision
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection.mask_rcnn import MaskRCNNPredictor

      
def get_instance_segmentation_model(num_classes):
    model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
    in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels
    hidden_layer = 256
    model.roi_heads.mask_predictor = MaskRCNNPredictor(in_features_mask,
                                                       hidden_layer,
                                                       num_classes)

    return model

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

num_classes = 2

model = get_instance_segmentation_model(num_classes)
model.to(device)
model.load_state_dict(torch.load('weight.pt', map_location=torch.device('cpu')))
model.eval()


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

trans = torchvision.transforms.ToTensor()
def process_image(image):
    image = Image.fromarray(image)
    image = trans(image)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # ret,th1 = cv2.threshold(image ,127,255, cv2.THRESH_BINARY)
    with torch.no_grad():
        prediction = model([image.to(device)])
    out = prediction[0]['masks'][0, 0].mul(255).byte().cpu().numpy()
    _, img_thresh = cv2.threshold(out, 200, 255, cv2.THRESH_BINARY)
    return img_thresh

def overlay_image(image, mask):
    original = image
    image = mask

    overlay = original.copy()
    output = original.copy()
    alpha = 0.3
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = np.array(image)
    _, img_thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    canny_output = cv2.Canny(img_thresh, 100, 100 * 2)
    contours, _ = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    inpaint_mask = np.zeros(original.shape, dtype=np.uint8)
    for contour in contours:
        cv2.drawContours(inpaint_mask,[contour], -1, (255, 0, 0), thickness=-1)
    res = cv2.addWeighted(inpaint_mask,0.3,overlay,0.7,0)
    #### add weigths for overlay and print it
    # cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)    
    # print("alpha={}, beta={}".format(alpha, 1 - alpha))
    # cv2.imshow("Output", output)
    res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
    return res

def ecze_score(mask):
    count = 0
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask[i,j] == 255:
                count += 1
    return int((count/(mask.shape[0]*mask.shape[1]))*100)

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

