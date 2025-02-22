# ==============================
# Import necessary Django modules and models
# ==============================
from base.models import Message


from django.shortcuts import render, redirect, get_object_or_404  # Handles rendering templates and redirections
from django.db.models import Q  # Allows complex query lookups
from django.http import HttpResponse  # Handles HTTP responses
from django.contrib.auth.decorators import login_required  # Ensures only logged-in users access certain views
from django.contrib.auth import authenticate, login, logout  # Handles authentication
from django.contrib import messages  # Displays flash messages
from django.contrib.auth.models import User  # User model for authentication
from django.contrib.auth.forms import UserCreationForm
from base.models import Room, Topic  # Import custom models
from base.forms import RoomForm  # Import Django form for Room model


# ==============================
# User Authentication Views
# ==============================

def loginPage(request):
    """
    Handles user login.
    Redirects authenticated users to the home page.
    """
    page = 'login'
    if request.user.is_authenticated:
        return redirect("home")  # Redirects logged-in users to home

    if request.method == 'POST':
        username = request.POST.get('username').lower() # Get username from form input
        password = request.POST.get('password')  # Get password from form input

        try:
            user = User.objects.get(username=username)  # Check if user exists
        except:
            messages.error(request, 'User does not exist')  # Error message if user not found
            return render(request, 'base/login_register.html')

        user = authenticate(request, username=username, password=password)  # Authenticate user

        if user is not None:
            login(request, user)  # Log in user
            return redirect('home')  # Redirect to home after login
        else:
            messages.error(request, 'Username or password is incorrect')  # Error for incorrect login

    context = {'page': page}
    return render(request, 'base/login_register.html', context)  # Render login page


# ==============================
# logout 
# ==============================

def logoutUser(request):
    """
    Logs out the user and redirects to the home page.
    """
    logout(request)
    return redirect('home')

# ==============================
# Sign up registeration
# ==============================

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('home')
        else :
            messages.error(request,'An error occured during registration')

    return render(request, 'base/login_register.html',{'form' : form} )  # Render registration page


# ==============================
# Home and Room Views
# ==============================

def home(request):
    """
    Displays the homepage with room listings and search functionality.
    """
    q = request.GET.get('q') if request.GET.get('q') != None else ''  # Get search query from URL

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |  # Filter by topic name
        Q(name__icontains=q) |  # Filter by room name
        Q(description__icontains=q)  # Filter by room description
    )

    topics = Topic.objects.all()  # Fetch all topics
    room_count = rooms.count()  # Count the number of rooms
    room_messages = Message.objects.all().filter(Q(room__topic__name__icontains = q))

    context = {'rooms': rooms, 'topics': topics,
                'room_count': room_count , 'room_messages' : room_messages}
    return render(request, 'base/home.html', context)  # Render home page


def room(request, pk):
    """
    Displays a specific room based on its ID.
    """
    room = Room.objects.get(id=pk)  # Fetch room by primary key (id)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()

    if request.method == "POST":
        message_body = request.POST.get("body")
        

        if message_body:
            message = Message.objects.create(
                user=request.user,  # ✅ Ensure the user is set
                room=room,  # ✅ Pass the correct room object
                body=message_body
            )
            room.participants.add(request.user)
            return redirect("room", pk=room.id)  # Redirect to avoid form resubmission

    context = {'room': room , 'room_messages' : room_messages ,
               'participants': participants}
    return render(request, 'base/room.html', context)  # Render room page



def userProfile(request, pk):

    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_message = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user' : user , 'rooms ': rooms , 'room_message' : room_message}
    return render(request , 'base/profile.html',context)
# ==============================
# CRUD Operations for Rooms
# ==============================



# ==============================
# create room
# ==============================
@login_required(login_url='login')  # Ensures only logged-in users can create rooms
def createRoom(request):
    """
    Allows authenticated users to create a room.
    """
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after creating room

    context = {'form': form}
    return render(request, 'base/room_form.html', context)  # Render room creation form


# ==============================
# update room
# ==============================


@login_required(login_url='login')  # Ensures only logged-in users can update rooms
def updateRoom(request, pk):
    """
    Allows the host of a room to update its details.
    """
    room = Room.objects.get(id=pk)  # Fetch the room by its ID
    form = RoomForm(instance=room)  # Pre-fill form with existing data

    if request.user != room.host:
        return HttpResponse('You are not allowed here..')  # Restrict unauthorized users

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after updating room

    context = {'form': form}
    return render(request, 'base/room_form.html', context)  # Render room update form

# ==============================
# delete room
# ==============================

@login_required(login_url='login')  # Ensures only logged-in users can delete rooms
def deleteRoom(request, pk):
    """
    Allows the host of a room to delete it.
    """
    room = get_object_or_404(Room, id=pk)  # ✅ Handle room not found properly
    room = Room.objects.get(id=pk)  # Fetch room by ID

    if request.user != room.host:
        return HttpResponse('You are not allowed here..')  # Restrict unauthorized users

    if request.method == 'POST':
        room.delete()
        return redirect('home')  # Redirect to home after deletion

    return render(request, 'base/delete.html', {'obj': room})  # Render delete confirmation page

@login_required(login_url='login')  

def deleteMessage(request, pk):
    """
    Allows to delete thw messages
    """
    message = Message.objects.get(id=pk)  # Fetch room by ID

    if request.user != message.user:
        return HttpResponse('You are not allowed here..') 
    if request.method == 'POST':
        message.delete()
        return redirect('home')  

    return render(request, 'base/delete.html', {'obj': message}) 
