from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

# Removi a restrição de superusuário pra você conseguir criar o primeiro
@csrf_protect
def create_superuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
        else:
            User.objects.create_superuser(username=username, email=email, password=password)
            messages.success(request, 'Superusuário criado com sucesso!')
            return redirect('create_superuser')

    return render(request, 'admin/create_superuser.html')
