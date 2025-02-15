from django.shortcuts import render, redirect


from base.models import Room

from base.forms import RoomForm


# Create your views here.
# rooms =[
#     {'id' : 1, 'name': 'lets go !'},
#     {'id' : 2, 'name': 'lets go honours !'},
#     {'id' : 3, 'name': 'lts go honours !'}

# ]




def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}

    return render(request , 'base/home.html',context)

def room(request,pk):
        room = Room.objects.get( id = pk)
        context = {'room' : room}
        return render(request , 'base/room.html' )

def createRoom(request):
      form = RoomForm()

      if request.method == 'POST':
            form =RoomForm(request.POST)

            if form.is_valid():
                  form.save()
                  return redirect('home')
            
      context = {'form':form}
      return render(request,'base/room_form.html', context)

def updateRoom(request,pk):
      room = Room.objects.get(id = pk)
      form = RoomForm(instance=room)
      context = {'form': form }
      
      return render(request , 'base/room_form.html',context)
       