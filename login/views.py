# from django.http import HttpResponse

# from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate
# from django.contrib.auth import login,logout

# def main(request):
#     return render(request,"main.html")

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

# def singup(request):
     
#  return render(request,"sinup.html")