import cv2
from django.core.files.base import ContentFile

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