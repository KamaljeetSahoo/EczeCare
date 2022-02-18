
![image](https://user-images.githubusercontent.com/79363736/154750683-51de5279-35c9-499a-9eb5-752574f91def.png)
# Project-EczeCare
### `THEME : PRECISION MEDICINE`

`Project-EczeCare` Project EczeCare is an Eczema tracking and analysis application to study infection and lifestyle changes in eczema patients and integrate caregiver and care receiver on a common platform while providing valuable insights like skin segmentation model for severity score calculation and certain mathematical models from POEM(Patient-Oriented Eczema Measure) score.

Contents
========

 * [Installation](#installation)
 * [Tech-Stacks Used](#Tech-Stacks-Used)
 * [Features Added](#Features-Added)
 * [Snapshots](#Snapshots)
 * [Demo](#Demo)
 


### Installation
---
1. Clone the repository
2. Open the Project Path where manage.py is present in python console. (ex-  C:\Users\jenaa\djangoproject\EczeCare)
3. Create a .env file where the subscription and API key need to go.
4. Run `pip install -r requirements.txt`
4. Run `python manage.py makemigrations` then `python manage.py migrate`.
5. In python console type, `python manage.py runserver`
6. The website link should be displayed on the side. Copy it and paste in the web browser.

`.env file datas hasn't been pushed`
<br/>


### Tech-Stacks Used
---
<ol>
<li> Django Templating language
<li>Django Rest Framework 
<br/>
<li>SQLite3
<br/>
<li>Jinja2
<br/>
<li>PyTorch 
<br/>
<li>OpenCV
<br/>
<li>Bootstrap CSS
<br/>
</ol>

### Features Added
---
<ol>
    
<li>Patient Assessment : Self assessment of patients via a questionnaire and calculating their Patient Oriented Eczema Measure(POEM) score.
</li></br>
<li>Weather dependency of infection : Our Mathematical model calculates the dependency of eczema severity of patients with rise and fall in weather conditions.</li></br>
<li>EczeImage : Recording the images of the patient’s skin as uploaded by them and based on the affected area , we calculate the severity of eczema and provide a segmented image (generated from our Deep Learning model) for the patient’s reference displayed as a carousel to show the improvements.
</li></br>
<li>Triggers : List of lifestyle habits that might worsen the skin condition of patient customisable by the patient.</li></br>
<li>POEM score : Patient Oriented Eczema Measure Score calculated from regular questionnaire.
</li></br>
<li>Insights : Representation of sleep, eczema and skin roughness condition of patient via user friendly graphs to study the improvement trends.
</li></br>
<li>Blogs : This platform can unlock new ways for people to stay better informed about skin disorders through expert-curated blogs.
</li></br>
<li>Consultation : In case of severe issues, we also provide the option to consult with doctors. Users can connect with doctors either through Video calling or Chatting.
</li></br>
<li>Doctor Portal : A separate doctor portal containing insights of the doctor's patient.
</li></br>
</ol>

### Snapshots
---
Some of the snapshots of website.
</br>
![Screenshot (321)](https://user-images.githubusercontent.com/79363736/154756737-5dd6ab6e-48ad-4813-a2d3-5098633a9e81.png)<br/> - Landing Page

![Screenshot (327)](https://user-images.githubusercontent.com/79363736/154758030-8814c915-dd88-4594-9d85-17fe82bf457c.png) <br/> - DashBoard with POEM Score and weather dependency

![Screenshot (328)](https://user-images.githubusercontent.com/79363736/154758229-6f1695f4-2bf6-4633-b2e3-0fb60b02cae7.png) <br/> - POEM questionnaire

![Screenshot (330)](https://user-images.githubusercontent.com/79363736/154758868-cc821375-191f-4aaf-a890-ff99e316d877.png) <br/> - Triggers List

![Screenshot (331)](https://user-images.githubusercontent.com/79363736/154758790-24ffca0a-b5b2-4a54-8843-ea3a64e6a2a4.png) <br/> - Insights

![Screenshot (332)](https://user-images.githubusercontent.com/79363736/154758683-d57a0185-1486-4ba1-bc0e-b046abc9cc35.png) <br/> - EczeImage Analysis

![Screenshot (334)](https://user-images.githubusercontent.com/79363736/154759244-744f93ba-e19b-4afa-8fd9-7cb07c7d2502.png) <br/> - Doctor's portal 

![Screenshot (335)](https://user-images.githubusercontent.com/79363736/154759379-69d3eece-74e2-4f5c-8968-a685fc37acf7.png) <br/> - Appointment confirmation

### Demo
---

[EczeCare_Demo](https://projecteczecare.pythonanywhere.com/)
### Weight file for DL Model
---
Drive Link : https://drive.google.com/file/d/1qKZwkmRWwLs5byPjOMegMUN5FIUhs8vB/view?usp=sharing
</br>
