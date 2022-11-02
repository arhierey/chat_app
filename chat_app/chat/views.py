from django.shortcuts import render, redirect
from chat.models import Room, Message, User
from django.http import HttpResponse, JsonResponse


def home(request):
    return render(request, 'home.html')


def choose_room(request):
    return render(request, 'choose_room.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    context = {'username': username,
               'room': room,
               'room_details': room_details
               }
    return render(request, 'room.html', context)


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)


def login(request):
    username = request.POST['username']
    password = request.POST['password']

    if User.objects.filter(name=username).exists():
        if User.objects.get(name=username).password == password:
            # return redirect('/choose_room')
            return render(request, 'choose_room.html', {'username': username})
        else:
            return HttpResponse('Incorrect password')
    else:
        return HttpResponse('Incorrect username')


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()

    return HttpResponse('Message sent successfully')


def get_messages(request, room):
    room_detailes = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_detailes.id)
    return JsonResponse({'messages': list(messages.values())})
