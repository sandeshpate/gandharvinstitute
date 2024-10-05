from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from admission.models import Admissionform

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.models import User

from myservice.models import ClassCard #this is home page of an service card section
from myservice.models import Play #this is an homepage slider

from myservice.models import Placement



from aboutus.models import SlidersImage  #this is an about slider
from aboutus.models import SliderssOne, SliderssTwo  #this is an about automatic slider
from aboutus.models import TeamMembers   #this is an team member 
from aboutus.models import AddCourseabout #add dropdwon for about
from myservice.models import Photo, Feature #this is an home page of an about sectionn #this is an home page of an about section
from coursepage.models import CourseContent #this is an course section
from coursepage.models import FeatureCard #this is an course feature section
from coursepage.models import Workshopnew #this is an workshop course section
# from myservice.models import Servicecard #this is an course service section
from myservice.models import AddCourse #add dropdwon for homepage
from coursepage.models import AddDropdownCourses  #add dropdwon for course
from coursepage.models import Servicecard #this is an course service section
from play.models import SliderImage
from dance.models import DanceSection
from dance.models import DanceFeature
from dance.models import Course,  Duration, Fee,CourseSyllabus
from dance.models import  CardSliderItem
from acting.models import ActingSection
from acting.models import  ActingFeature
from acting.models import Acting, ActDuration, ActingFee
from acting.models import  ActingSyllabus
from acting.models import ActingCardSliderItem
from set.models import setSection
from set.models import  setFeature
from set.models import setcourse, setDuration,setFee
from set.models import   setCourseSyllabus
from set.models import setCardSliderItem
from costume.models import costumeSection
from costume.models import  costumeFeature
from costume.models import costumecourse, costumeDuration,costumeFee
from costume.models import  costumeCourseSyllabus
from costume.models import costumeCardSliderItem

from singing.models import singingSection
from singing.models import  singingFeature
from singing.models import singingcourse, singingDuration,singingFee
from singing.models import singingCourseSyllabus
from singing.models import singingCardSliderItem
from flimmaking.models import flimSection
from flimmaking.models import  flimFeature
from flimmaking.models import flimcourse, flimDuration,flimFee
from flimmaking.models import flimCourseSyllabus
from flimmaking.models import flimCardSliderItem
from dashboard.models import dashCourse



   



    











def homepage(request):
    cards = ClassCard.objects.all()
    plays = Play.objects.all()
    photos = Photo.objects.all()
    features = Feature.objects.all()
    dropdown = AddCourse.objects.all()
    placements = Placement.objects.all()
    context = {
        'cards': cards,
        'plays': plays,
        'photos': photos, 
        'features': features,
        'dropdown': dropdown,
        'placements': placements
        
    }

    return render(request, 'index.html', context)






 


def about(request):
    slider_images = SlidersImage.objects.all()
    slider_one_images = SliderssOne.objects.all()
    slider_two_images = SliderssTwo.objects.all()
    team_members = TeamMembers.objects.all()
    aboutdropdowns = AddCourseabout.objects.all()
   
   
    
    context ={
        'slider_images': slider_images,
        'slider_one_images': slider_one_images,
        'slider_two_images': slider_two_images,
        'team_members': team_members,
        'aboutdropdowns': aboutdropdowns,
         
       
        
       

    }
    # return HttpResponse("welcome to home pages")
    # return render(request,"aboutus.html")
    return render(request, 'aboutus.html', context)
  
def course(request): 
    
    course_contents = CourseContent.objects.all().order_by('order_index')
    course_cards = FeatureCard.objects.all().order_by('number')
    workshop = Workshopnew.objects.first()  # Assuming there's only one record; adjust as necessary
    services = Servicecard.objects.all()
    coursedrop =  AddDropdownCourses.objects.all()

    context = {

         'course_contents':  course_contents,
         'course_cards': course_cards,
        'workshop': workshop,
        'services': services,
        'coursedrop': coursedrop,
     }
    # return HttpResponse("welcome to home pages")
    return render(request,"course.html",context)

# def main(request):
#     return render(request,"main.html")
# views.py


def main(request):
    return render(request, 'main.html')  # Create a simple home.html template

# def signin(request):
#     if request.method=="post":
#         username=request.post['username']
#         password=request.post['password']
#         user=authenticate(username=username,password=password)
#         if user:
#             login(request,user)
#             return redirect("main/")
#         else:
#             return HttpResponse ("Username or Password is incorrect!!!")
#     # else:
#     #     return redirect("main/")   
   
   

#     # return HttpResponse("welcome to home pages")
#     return render(request,"login.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
          
            return redirect('dashboard')  # redirect to a home page after login
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')
def singout(request):
    logout(request)
    return redirect('sing')

# def singup(request):
     

   
  
#     # return HttpResponse("welcome to home pages")
#     return render(request,"sinup.html")





def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'signup.html')

        # Check if the email is already used
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'signup.html')

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Success message to be shown after redirecting to the login page
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')  # Redirect to login after successful signup

    return render(request, "signup.html")

def play(request):
    slider_images = SliderImage.objects.all()
    context = {
     'slider_images': slider_images,
    }
    # return HttpResponse("welcome to home pages")
    return render(request,"play.html",context)
def dancing(request):
    # return HttpResponse("welcome to home pages")
    content = DanceSection.objects.first() 
    features =  DanceFeature.objects.all()
    courses = Course.objects.all()
    durations = Duration.objects.all()
    fees = Fee.objects.all()
    syllabus = CourseSyllabus.objects.all() 
    slider_items = CardSliderItem.objects.all()

    context={
        'content': content,
        'features': features,
        'courses': courses,
        'durations': durations,
        'fees': fees,
        'syllabus': syllabus,
        'slider_items': slider_items,
       
       
    }
    return render(request, 'dancing.html',context)

def set(request):
    # return HttpResponse("welcome to home pages")
    
    content = setSection.objects.first() 
    features =  setFeature.objects.all()
    courses = setcourse.objects.all()
    durations = setDuration.objects.all()
    fees = setFee.objects.all()
    syllabus = setCourseSyllabus.objects.all() 
    setslider_items = setCardSliderItem.objects.all()

    context={
        'content': content,
        'features': features,
        'courses': courses,
        'durations': durations,
        'fees': fees,
        'syllabus': syllabus,
        'setslider_items': setslider_items,
       
       
    }
    return render(request, 'set.html',context)
  


def singing(request):

     
    content = singingSection.objects.first() 
    features =  singingFeature.objects.all()
    courses = singingcourse.objects.all()
    durations = singingDuration.objects.all()
    fees = singingFee.objects.all()
    syllabus =  singingCourseSyllabus.objects.all() 
    singingslider_items = singingCardSliderItem.objects.all()

    context={
        'content': content,
        'features': features,
        'courses': courses,
        'durations': durations,
        'fees': fees,
        'syllabus': syllabus,
        'singingslider_items': singingslider_items,
       
       
    }
    # return HttpResponse("welcome to home pages")
    return render(request,"singing.html",context)

def costume(request):

    # return HttpResponse("welcome to home pages")
    content = costumeSection.objects.first() 
    features =  costumeFeature.objects.all()
    courses = costumecourse.objects.all()
    durations = costumeDuration.objects.all()
    fees = costumeFee.objects.all()
    syllabus = costumeCourseSyllabus.objects.all() 
    costumeslider_items = costumeCardSliderItem.objects.all()

    context={
        'content': content,
        'features': features,
        'courses': courses,
        'durations': durations,
        'fees': fees,
        'syllabus': syllabus,
        'costumeslider_items': costumeslider_items,
       
       
    }
    return render(request,"costume.html",context)
def acting(request):
    # return HttpResponse("welcome to home pages")
    
    content = ActingSection.objects.first() 
    features =  ActingFeature.objects.all()
    courses = Acting.objects.all()
    durations = ActDuration.objects.all()
    fees = ActingFee.objects.all()
    syllabus = ActingSyllabus.objects.all() 
    actslider_items = ActingCardSliderItem.objects.all()

    context={
        'content': content,
        'features': features,
        'courses': courses,
        'durations': durations,
        'fees': fees,
        'syllabus': syllabus,
        'actslider_items': actslider_items,
       
       
    }
    return render(request, 'acting.html',context)
  



def flimmaking(request):
    # return HttpResponse("welcome to home pages")

    content = flimSection.objects.first() 
    features =   flimFeature.objects.all()
    courses = flimcourse.objects.all()
    durations = flimDuration.objects.all()
    fees = flimFee.objects.all()
    syllabus = flimCourseSyllabus.objects.all() 
    flimslider_items = flimCardSliderItem.objects.all()

    context={
        'content': content,
        'features': features,
        'courses': courses,
        'durations': durations,
        'fees': fees,
        'syllabus': syllabus,
        'flimslider_items': flimslider_items,
       
       
    }
    return render(request,"flimmaking.html",context)
def dashboard(request):
    
    # return HttpResponse("welcome to home pages")
    return render(request,"dashhome.html")
def dashboardcourse(request):

    dashcourses = dashCourse.objects.all()

    context={
        'dashcourses': dashcourses,
    }
    return render(request, "dashboardcourse.html", context)

    # return HttpResponse("welcome to home pages")
    
def dashhelp(request):
    
    # return HttpResponse("welcome to home pages")
    return render(request,"dashhelp.html")
def dashprofile(request):
    
    # return HttpResponse("welcome to home pages")
    return render(request,"dashprofile.html")
def dashregister(request):
    
    if request.method == "POST":
        admission = Admissionform(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            dob=request.POST['dob'],
            gender=request.POST['gender'],
            contact=request.POST['contact'],
            email=request.POST['email'],
            father_name=request.POST['father_name'],
            father_occupation=request.POST['father_occupation'],
            father_mobile=request.POST['father_mobile'],
            mother_name=request.POST['mother_name'],
            mother_occupation=request.POST['mother_occupation'],
            mother_mobile=request.POST['mother_mobile'],
            permanent_address=request.POST['permanent_address'],
            temporary_address=request.POST.get('temporary_address', ''),
            street_address=request.POST['street_address'],
            pincode=request.POST['pincode'],
            state=request.POST['state'],
            city=request.POST['city'],
            country=request.POST['country'],
            previous_school=request.POST['previous_school'],
            qualification=request.POST['qualification'],
            degree_name=request.POST['degree_name'],
            previous_training=request.POST.get('previous_training', ''),
            theatre_experience=request.POST.get('theatre_experience', ''),
            performance_experience=request.POST.get('performance_experience', ''),
            special_skills=request.POST.get('special_skills', ''),
            acting_group=request.POST.get('acting_group', ''),
            desired_course=request.POST['desired_course'],
            experience_level=request.POST['experience_level'],
            photo=request.FILES['photo'],
            drama_certificate=request.FILES['drama_certificate'],
        )
        admission.save()
        messages.success(request, "Your application is approved!")
        return redirect('dash')  # Redirect after successful submission
    

    
  


    # return HttpResponse("welcome to home pages")
    return render(request,'dashregister.html')
def dashteacher(request):
    
    # return HttpResponse("welcome to home pages")
    return render(request,"dashteacher2.html")
def dashupdate(request):
    
    # return HttpResponse("welcome to home pages")
    return render(request,"dashupdate.html")
def contact(request):
    
    # return HttpResponse("welcome to home pages")
    return render(request,"contacts.html")
def courseme(request):
    return HttpResponse("course pate")