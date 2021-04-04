from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
#users 경로의 urls.py에서 default로 지정한 path
#그 path 에서 호출한 함수를 구현한다.

def main(request):
    #template의 users/main.html을 호출할 것이라는 뜻이다.
    if request.method == 'GET':
        return render(request,'users/main.html')
    elif request.method == 'POST':
        return loginRoutine(request)


def loginRoutine(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect(reverse('posts:index'))
    else:
        # Return an 'invalid login' error message.
        return render(request, 'users/main.html')