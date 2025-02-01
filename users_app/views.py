from django.shortcuts import render,redirect
from users_app.forms import CustomUserForm
from django.contrib import messages

# Create your views here.

def register(request):
    
    if request.method == "POST":
        registration_form = CustomUserForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, ('New User created successfully, Login to Get Started!'))
            return redirect('register')
    else:
        registration_form = CustomUserForm()
        return render(request, 'register.html', {'registration_form': registration_form})