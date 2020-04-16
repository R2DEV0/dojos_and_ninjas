from django.shortcuts import render, redirect
from .models import Ninja, Dojo

def index(request):
  
    ninja = Ninja.objects.all()
    dojo = Dojo.objects.all()

    context= {
        'ninja': ninja,
        'dojo': dojo, 
    }

    return render(request, 'index.html', context)


def show(request):
    print(Dojo.objects.all())
    print(Ninja.objects.all())

    return redirect('/')


def submit_ninja(request):
    dojo_id = request.POST['dojo']
    dojo_from_form= Dojo.objects.get(id=dojo_id)
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    
    Ninja.objects.create(first_name=first_name, last_name=last_name,dojo=dojo_from_form)

    return redirect('/show')


def submit_dojo(request):
    name=request.POST['name']
    city=request.POST['city']
    state=request.POST['state']
    Dojo.objects.create(name=name, city=city, state=state)

    return redirect('/show')