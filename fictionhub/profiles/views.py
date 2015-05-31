from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User
from .forms import RegistrationForm, UserForm

def subscribe(request, username):
    userprofile = User.objects.get(username=username)
    if not request.user.is_anonymous():
        user = request.user
        user.subscribed_to.add(userprofile)
        user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    else:
        return HttpResponseRedirect('/login/')    

def unsubscribe(request, username):
    userprofile = User.objects.get(username=username)    
    user = request.user
    user.subscribed_to.remove(userprofile)
    user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

def about(request, username):
    userprofile = get_object_or_404(User, username=username)    
    subscribed_to = request.user.subscribed_to.all()
    return render(request, 'profiles/about.html',{
        'userprofile':userprofile,
        'subscribed_to':subscribed_to
    })

def preferences(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/preferences/')            
    else:
        form = UserForm(instance=request.user)
    
    return render(request, "profiles/prefs.html", {
        'form': form
    })


def login_or_signup(request):
    # If already logged in - get out of here
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    authenticate_form = AuthenticationForm(None, request.POST or None)
    # register_form = UserCreationForm()
    register_form = RegistrationForm()
    register_form.fields['password1'].widget.attrs['placeholder'] = "Password"
    register_form.fields['password2'].widget.attrs['placeholder'] = "Repeat Password"        
    return render(request, "profiles/login.html", {
        'authenticate_form': authenticate_form,
        'register_form': register_form,        
    })


# Only log in
def authenticate_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
 
    # Initialize the form either fresh or with the appropriate POST data as the instance
    auth_form = AuthenticationForm(None, request.POST or None)
 
    # Ye Olde next param so common in login.
    # I send them to their default profile view.
    nextpage = request.GET.get('next', '/')
 
    # The form itself handles authentication and checking to make sure passowrd and such are supplied.
    if auth_form.is_valid():
        login(request, auth_form.get_user())
        return HttpResponseRedirect(nextpage)
 
    return render(request, 'profiles/authenticate.html', {
        'form': auth_form,
        'title': 'User Login',
        'next': nextpage,
    })


# Only sign up
def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # new_user = form.save()
            user = User.objects.create_user(form.cleaned_data['username'], None, form.cleaned_data['password1'])
            user.save()

            # log user in after signig up
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "profiles/register.html", {
        'form': form,
    })
