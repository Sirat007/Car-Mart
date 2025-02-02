from django.shortcuts import render,redirect
from .forms import RegisterForm,ChangeUserData
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Cars.models import Order

# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        
        else:
            form = RegisterForm()
    
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('homepage')

class UserLogin(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self,form):
        messages.success(self.request,'Logged in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,'Logged In information is incorrect')
        return super().form_invalid(form)
    
@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'profile.html',{'orders':orders})

@login_required
def editprofile(request):
    if request.method == 'POST':
        profile_form = ChangeUserData(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('homepage')
    else:
        profile_form = ChangeUserData(instance = request.user)
    return render(request,'edit_profile.html',{'form':profile_form})

def UserLogout(request):
    logout(request)
    return redirect('homepage')