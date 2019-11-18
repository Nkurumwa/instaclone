from django.shortcuts import render,redirect
from .models import Image, Profile,Comment
from django.contrib.auth.models import User
from .forms import CommentForm, ImageForm, ProfileUpdateForm, UserUpdateForm, PostIMageForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from .email import 