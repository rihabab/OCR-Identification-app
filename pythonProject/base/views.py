import os
import sys
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from .models import IdCard
import pytesseract

from base.face_test import testing
from base.process import processing

import PIL.Image
import cv2
import shutil


import easyocr
sys.stdout.reconfigure(encoding='utf-8')
reader = easyocr.Reader(['en', 'fr'])

# Create your views here.


def loginPage(request):
    context={}
    if request.user.is_authenticated :
        return render(request, 'base/home.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = User.objects.get(username=username)
            except:
                # messages.error(request, "User does not exist !!")
                context['res']='User name or password invalide!'
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # messages.error(request, "Username or password does not exist !!")
                context['res']='User name or password invalide!'
        
        return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    if request.user.is_authenticated :
        return render(request, 'base/home.html')
    else:
        context={}
        return render(request, 'base/login.html', context)

   
def uploadFile(request):
    if request.user.is_authenticated :
        context = {}
        if request.method == 'POST':
            if 'document' in request.FILES:
                uploaded_file = request.FILES['document']
                fs = FileSystemStorage()
                name = fs.save(uploaded_file.name, uploaded_file)
                context['url'] = fs.url(name)
                image_path = 'C:/Users/Rihab/PycharmProjects/pythonProject/pythonProject/' + context['url']
                print(image_path)
                img = cv2.imread(image_path)
                def grayscale(image):
                    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                gray_image = grayscale(img)
                cv2.imwrite(r"C:\Users\Rihab\PycharmProjects\pythonProject\pythonProject\media\temp\gray.jpg", gray_image)

                            
                text1 = pytesseract.image_to_data(gray_image, output_type='data.frame')
                text = text1[text1.conf != -1]
                grouped_lines = text.groupby(['block_num', 'par_num', 'line_num'])
                text_lines = []
                for _, group in grouped_lines:
                    sorted_group = group.sort_values(by='left')  
                    text_line = ' '.join(sorted_group.text)
                    text_lines.append(text_line)


                array=[]
                i=0
                for line in text_lines:
                    array.append(line.split(" "))
                    i+=1
                    print(line)
                print(array)

                dict = {}

                dict['pays'] = array[0][0]+" "+array[0][1]+" "+array[0][2]
                dict['type'] = array[0][3]+" "+array[0][4]+" "+array[0][5]
                dict['nom'] = array[2][0]
                dict['prénom'] = array[3][0]
                dict['sexe'] = array[6][0]
                dict['Nationalité'] = array[6][1]
                dict['Taille'] = array[6][2]
                dict['Teint'] = array[6][3]
                dict['Datedenaissance'] = array[6][4]
                dict['Cheveux'] = array[8][0]
                dict['yeux']=array[10][0]
                dict['Adresse'] = array[8][1]+array[10][1]+array[10][2]
                dict['signesparticuliers'] = array[12][0]
                dict['numerodetelephone'] = array[12][1]+array[12][2]+array[12][3]+array[12][4]
                dict['Actedenaissance'] = array[16][0]+array[16][1]
                dict['duon'] = array[16][2]
                dict['Ndedoc'] = array[18][0]
                dict['Expiration'] = array[18][1]
                dict['Délivréeà'] = array[20][1]

                # p_name= dict['nom'] + "_" + dict['prénom'] + ".jpg"
                # new_image_path = os.path.join('C:/Users/Rihab/PycharmProjects/pythonProject/pythonProject/base/known_faces/', p_name)
                # os.rename(image_path, new_image_path)

                context['array'] = array

                context['dict'] = dict
            elif 'nom' in request.POST :
                lastname = request.POST.get('nom')
                firstname = request.POST.get('prénom')
                country = request.POST.get('pays')
                typecard = request.POST.get('type')
                sex = request.POST.get('sexe')
                nationality = request.POST.get('nationalité')
                height = request.POST.get('taille')
                color = request.POST.get('teint')
                dateofbirth = request.POST.get('Datedenaissance')
                haircolor = request.POST.get('Cheveux')
                eyecolor = request.POST.get('yeux')
                adress = request.POST.get('Adresse')
                mark = request.POST.get('signesparticuliers')
                phonenumber = request.POST.get('numerodetelephone')
                birthcertificate = request.POST.get('Actedenaissance')
                du = request.POST.get('duon')
                docnumber = request.POST.get('Ndedoc')
                expiry = request.POST.get('Expiration')
                placeofissue = request.POST.get('Délivréeà')
                user = request.user
                image_path = request.POST.get('image_path')

                


                IdCard.objects.create(
                    country=country,
                    typecard=typecard,
                    firstname=firstname,
                    lastname=lastname,
                    sex=sex,
                    nationality=nationality,
                    height=height,
                    color=color,
                    dateofbirth=dateofbirth,  
                    haircolor=haircolor,
                    eyecolor=eyecolor,
                    adress=adress,          
                    mark=mark,
                    phonenumber=phonenumber,
                    birthcertificate=birthcertificate,
                    du=du,
                    docnumber=docnumber,
                    expiry=expiry,
                    placeofissue=placeofissue,
                    user=user
                )
                messages.success(request, 'user identified successfuly')



                destination_directory = 'C:/Users/Rihab/PycharmProjects/pythonProject/pythonProject/base/known_faces'
                new_name = lastname + '_' + firstname +'.jpg'
                destination_path = os.path.join(destination_directory, new_name)
                image_path='C:/Users/Rihab/PycharmProjects/pythonProject/pythonProject/' + image_path
                print(image_path)
                if os.path.exists(image_path):
                    print('exists')
                    if os.path.exists(destination_path):
                        print("The image exists.")
                    else:
                        shutil.copy2(image_path, destination_path)
                        processing()
                else :
                    print('does not exist')

                


                # processing()


        return render(request, 'base/upload.html', context)
    else:
        context={}
        return render(request, 'base/login.html', context)
def recognition(request):
    context = {}
    if request.user.is_authenticated :
        if request.method == 'POST':
            if 'document' in request.FILES:
                uploaded_file = request.FILES['document']
                fs = FileSystemStorage()
                name = fs.save(uploaded_file.name, uploaded_file)
                context['url'] = fs.url(name)
                image_path = 'C:/Users/Rihab/PycharmProjects/pythonProject/pythonProject' + context['url']
                print(image_path)
                # image_path = os.path.join(r"C:\Users\Rihab\PycharmProjects\pythonProject\pythonProject\base\recognition", name)
                

                
                result=testing(image_path)
                print(result)
                if result == None : 
                    context['res']='No faces found in the image! Provide a clear one.'
                elif result == 'Unknown':
                    context['res']='The face does not belong to any of our users.'
                else :
                    context['result']=testing(image_path)
                    print(context['result'])
                    s = context['result']
                    parts = s.split("_")
                    print(parts)  
                    lastname=parts[0]
                
                try:
                    card = IdCard.objects.filter(lastname=lastname).first()
                    context['dict']= card
                    print('card')
                    print(context['dict'])
                except:
                    print('unknown')



                
        return render(request, 'base/recognition.html', context)
    else:
        return render(request, 'base/login.html', context)
    


