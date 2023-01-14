from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth  import authenticate,  login, logout 
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import *
from prediction import cpy
# Create your views here.
# def home(request):
#     return render(request, 'index.html')

def Register(request):
    if request.method != "POST":
        return render(request, "register.html")
    username = request.POST['username']
    email = request.POST['email']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 != password2:
        messages.error(request, "Passwords do not match.")
        return redirect('/register')

    user = User.objects.create_user(username, email, password1)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    return render(request, 'login.html')

def Login(request):
    if request.method != "POST":
        return render(request, "login.html")
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, "Successfully Logged In")
        return render(request ,'after_login.html')
    else:
        messages.error(request, "Invalid Credentials")
    return render(request ,'after_login.html')


def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')

def user_v(request):  # sourcery skip: extract-method
    if request.method == "POST":
        fm = user_status(request.POST,request.FILES)
        if fm.is_valid():
            reg=user_details(name=fm.cleaned_data['name'],age=fm.cleaned_data['age'],image1=fm.cleaned_data['image1'],image2=fm.cleaned_data['image2'],gender=fm.cleaned_data['gender'],mail_id=fm.cleaned_data['mail_id'])
            reg.save()
            return HttpResponseRedirect("/")
    else:
        fm = user_status()
    return render(request, "index.html", {'form':fm})

def reports(request,myid):
    data = user_details.objects.filter(id=myid)
    image1 = data.get().image1
    img = cpy.get_image(image1)
    if img=='normal':
        prescription='you are all fit'
    elif img=='diabetic_retinopathy':
        prescription='''Diabetic retinopathy (die-uh-BET-ik ret-ih-NOP-uh-thee) is a diabetes complication that affects eyes. It's caused by damage to the blood vessels of the light-sensitive tissue at the back of the eye (retina).
        At first, diabetic retinopathy might cause no symptoms or only mild vision problems. But it can lead to blindness.
        If you having these symptoms then check up to doctor:
        Spots or dark strings floating in your vision (floaters)
        Blurred vision.
        Fluctuating vision.
        Dark or empty areas in your vision.
        Vision loss
        '''
    elif img=='glaucoma':
        prescription='''Glaucoma is a group of eye conditions that damage the optic nerve. The optic nerve sends visual information from your eye to your brain and is vital for good vision. Damage to the optic nerve is often related to high pressure in your eye. But glaucoma can happen even with normal eye pressure.Glaucoma can occur at any age but is more common in older adults. It is one of the leading causes of blindness for people over the age of 60.
        If you having these symptoms then check up to doctor:
        Severe headache.
        Severe eye pain.
        Nausea or vomiting.
        Blurred vision.
        Halos or colored rings around lights.
        Eye redness.
        '''
    elif img=='cataract':
        prescription='''A cataract is a clouding of the normally clear lens of the eye. For people who have cataracts, seeing through cloudy lenses is a bit like looking through a frosty or fogged-up window. Clouded vision caused by cataracts can make it more difficult to read, drive a car (especially at night) or see the expression on a friend's face.
        If you having these symptoms then check up to doctor:
        Clouded, blurred or dim vision.
        Increasing difficulty with vision at night.
        Sensitivity to light and glare.
        Need for brighter light for reading and other activities.
        Seeing "halos" around lights.
        Frequent changes in eyeglass or contact lens prescription.
        Fading or yellowing of colors
        '''
    else:
        prescription='please upload a clear image and try again'
    return render(request, "reports.html",{ 'data':data,'img':img,'pres':prescription})
def home(request):
    return redirect('/login')