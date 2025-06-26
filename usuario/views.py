from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('user_register')

    return render(request, 'usuario/register.html')
