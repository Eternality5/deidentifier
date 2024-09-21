from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class StaffLogin(View):
    template_name = 'auth/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, email=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            # Redirect to staff dashboard or desired page
            return redirect('auth/index.html')

        else:
            messages.success(request, ("Incorrect username or password, Try again ! "))
            return render(request, self.template_name)



def index(request):
    return render(request, 'auth/index.html')


# class LoginStaff(LoginView):
#     template_name = "auth/login.html"

# class Index(LoginRequiredMixin, CreateView):
#     def 


# def login_staff(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         print(username + " "+ " password")
#         user = authenticate(request, username=username , password=password)
#         if user is not None:
#             login(request, user)
#             return render(request, 'auth/login.html', {})
            
#         else:
#             messages.success(request, ("Incorrect username or password, Try again ! "))
#             return render(request, 'auth/login.html')
#     else:
#         return render(request, 'auth/login.html')


