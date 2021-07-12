from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    hello_world_list = HelloWorld.objects.all()

    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # Hello_World 테이블 내용 싹 긁어오기
        hello_world_list = HelloWorld.objects.all()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

    return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
