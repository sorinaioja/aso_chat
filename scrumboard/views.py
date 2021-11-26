from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from scrumboard.models import Room, Message

from .models import Message

# Create your views here.
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user )

            return redirect('login')
    context={'form': form}
    return render(request, 'scrumboard/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect')

    context={}
    return render(request, 'scrumboard/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


login_required
def home(request):
    context = {}
    return render(request, 'scrumboard/home.html', context)

def page0(request):
    context = {}
    return render(request, 'scrumboard/welcome.html', context)


def index(request):
    return render(request, 'scrumboard/index.html')


login_required(login_url='login')
def room(request, room):
    if request.user.is_authenticated:
        #username = request.GET.get('username')
        user = request.user
        username = user.username
        room_details = Room.objects.get(name=room)
        return render(request, 'scrumboard/room.html', {
            'username': username,
            'room': room,
            'room_details': room_details
        })
    else:
        return redirect('login')


login_required
def checkview(request):
    if request.user.is_authenticated:
        room = request.POST['room_name']
        #username = request.POST['username']
        user = request.user
        username = user.username
        if Room.objects.filter(name=room).exists():
            return redirect('/'+room+'/?username='+username)
        else:
            new_room = Room.objects.create(name=room)
            new_room.save()
            return redirect('/'+room+'/?username='+username)
    else:
        return redirect('login')


login_required
def send(request):
    if request.user.is_authenticated:
        message = request.POST['message']
        username = request.POST['username']
        room_id = request.POST['room_id']
        user = request.user

        new_message = Message.objects.create(value=message,username=username, user=user, room=room_id)
        new_message.save()
        return HttpResponse('Message sent successfully')
    else:
        return redirect('login')

login_required
def getMessages(request, room):
    if request.user.is_authenticated:
        room_details = Room.objects.get(name=room)

        messages = Message.objects.filter(room=room_details.id)
        return JsonResponse({"messages":list(messages.values())})
    else:
        return redirect('login')