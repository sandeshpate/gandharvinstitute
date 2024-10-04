"""
URL configuration for gandharvinstitute project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from gandharvinstitute import views








urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',views.main,name="main"),
    path('', views.homepage, name="home"),
    path('about/', views.about, name="aboutus"),
    path('course/', views.course, name="course"),
    path('login/', views.login_view, name="login"),
    path('sing/', views. signup_view, name="sing"),
    path('singout/',views.singout,name="singout"),
    path('play/', views.play, name="play"),
    path('dancing/', views.dancing, name="dancing"),
    path('acting/', views.acting, name="acting"),
    path('singing/', views.singing, name="acting"),
    path('costume/', views.costume, name="acting"),
    path('set/', views.set, name="acting"),
    path('flimmaking/', views.flimmaking, name="flimaking"),
    path('dash/', views.dashboard, name="dashboard"),
    path('dashcourse/', views.dashboardcourse, name="dashboardcourse"),
    path('dashprofile/', views.dashprofile, name="profile"),
    path('dashregister/', views.dashregister, name="dashregister"),
    path('dashtrainer/', views.dashteacher, name="teacher"),
    path('dashupdate/', views.dashupdate, name="update"),
    path('dashhelp/', views.dashhelp, name="help"),

    # path('homepage/',views.homepage),
    path('course-me/', views.courseme),
   
   
]





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)