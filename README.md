# Project- EczeCare
### `THEME : PRECISION MEDICINE`

<ol>
<li>Objective: We built a web app for systematic tracking of skin condition and consistent care of eczema patients.</li>
<br/>

<li>Implementation: With the aid of Deep Learning and neural networks the application would provide a robust synopsis of the usual causes of flares and triggers in eczema patients by analysing their routine life so that eczema patients can give attention to having a better quality of life without having to manually track their daily recovery and outbursts</li>
<br/>

<li>Application: We implemented deep learning techniques with other web technologies to provide an accessible solution to everyone. Along with guided supervision by a professional practitioner by a User Interface designed for both caretaker and patient</li>
<br/>

<li>Result and Aim: We offered end-to-end treatment to the afflicted users providing features such as Analyzing skin disease, Consultation with experts, AR skin model view, a blog community, and many more incorporated features.</li>
<br/>

### Instructions 
  <ol>
    <li> Make virtual Enviroment using conda or virtualenv </li> <br/>
    <li> pip install -r requirements.txt </li> <br/>
    <li> python manage.py makemigrations </li> <br/>
    <li> python manage.py migrate python </li> <br/>
    <li> manage.py runserver </li> <br/>

Contents
========

 * [Demo](#)
 * [Tech-Stacks Used](#Tech-Stacks-Used)
 * [Features Added](#)
 * [Deep Dive] (#)
 * [Snapshots](#Snapshots)


### Working Demo of our App
---

[EczeCare_Demo](https://projecteczecare.pythonanywhere.com/)

### Tech-Stacks Used
---
<ol>
<li>Django
<li>SQLite
<br/>
<li>Jinja2
<br/>
<li>Pytorch
<br/>
<li>OpenCV
<br/>
</ol>

### Features of Our Project!
---
<ol>
    
<li>✅ PATIENT ASSESSMENT:
Self assessment of patients via a questionnaire and calculating their Patient Oriented Eczema Measure(POEM) score. POEM is recommended by the  HOME (Harmonising Outcome Measures for Eczema) initiative as the core outcome instrument for measuring patient-reported symptoms in eczema trials.
<br/>
Recording the images of the patient’s skin as uploaded by them and based on the affected area , we calculate the severity of eczema and provide a segmented image (generated from our Deep Learning model) for the patient’s reference displayed as a carousel to show the improvements.
</li></br>
<li>✅Consultation: In case of severe issues, we also provide the option to consult with doctors. Users can connect with doctors either through Video calling or Chatting.</li></br>
<li>✅ Our Mathematical model calculates the dependency of eczema severity of patients with rise and fall in weather conditions.</li></br>
<li>✅ The image classification model is integrated with a web app. There is an option to either click a picture or upload a  saved one.
</li></br>
<li>✅Blogs: This platform can unlock new ways for people to stay better informed about skin disorders through expert-curated blogs.

</ol>

### AI Solution Deep dive
---
<ol>
    
<li>✅   ECZEMA DATASET: 
Due to poor availability of eczema dataset, we collected the available images for eczema and via Data Augmentation prepared the dataset
</li></br>
<li>✅MASK RCNN FOR SEGMENTATION:
	
Mask R-CNN is a state of the art model for instance segmentation, developed on top of Faster R-CNN. Faster R-CNN is a region-based convolutional neural networks, that returns bounding boxes for each object and its class label with a confidence score.
</li></br>
</ol>

### Snapshots
---
Some of the snapshots of website.
</br>

