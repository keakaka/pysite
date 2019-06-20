from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from guestbook.models import Guestbook


def list(request):
    guestbooklist = Guestbook.objects.all().order_by('-id')

    data = {'guestbooklist': guestbooklist}
    return render(request, 'guestbook/list.html', data)


def insert(request):
    guestbook = Guestbook()

    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.content = request.POST['content']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')


def deleteform(request, id=0):
    data = {'id': id}
    return render(request, 'guestbook/deleteform.html', data)


def delete(request):
    Guestbook.objects.\
        filter(id=request.POST['id']).\
        filter(password=request.POST['password']).delete()

    return HttpResponseRedirect('/guestbook')
