from django.shortcuts import render,redirect
from .models import Image, Profile,Comment
from django.contrib.auth.models import User
from .forms import CommentForm, ImageForm, ProfileUpdateForm, UserUpdateForm, PostIMageForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from .email import 


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            
            # email = form.cleaned_data['email']
            # recipient = NewsLetterRecipients(name = name,email =email)
            # recipient.save()
            # send_welcome_email(name,email)

            return redirect('/accounts/login/')
            
    else:
        form = UserRegisterForm()
    return render(request, 'registration/registration_form.html', {'form':form})


def home(request):
    return render(request, 'base.html')