from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage

import pytesseract
import PIL.Image
import cv2

import os


# Create your views here.


def loginPage(request):
    if request.user.is_authenticated :
        return render(request, 'base/home.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, "User does not exist !!")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Username or password does not exist !!")
        context={}
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
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)

    
            myconfig = r"--psm 11 --oem 3"
            


            image_path = os.path.join(r"C:\Users\Rihab\PycharmProjects\pythonProject\pythonProject\media", name)

            # text = pytesseract.image_to_string(PIL.Image.open(image_path), config=myconfig)
            
            
            img = cv2.imread(image_path)




            def grayscale(image):
                return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray_image = grayscale(img)
            cv2.imwrite(r"C:\Users\Rihab\PycharmProjects\pythonProject\pythonProject\media\temp\gray.jpg", gray_image)

            path = os.path.join(r"C:\Users\Rihab\PycharmProjects\pythonProject\pythonProject\media", "temp/gray.jpg")

            text = pytesseract.image_to_string(PIL.Image.open(path), config=myconfig)


            
            
            context['text'] = text



        return render(request, 'base/upload.html', context)
    else:
        context={}
        return render(request, 'base/login.html', context)
