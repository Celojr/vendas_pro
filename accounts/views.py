from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redireciona para o login após o registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
