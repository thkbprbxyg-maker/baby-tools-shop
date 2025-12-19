from django.shortcuts import redirect, render
from . forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def user_register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Konto wurde erfolgreich erstellt.')
            return redirect('login')
    else:
        form=RegisterForm()

    return render(request,'register.html',{'form':form})
def user_login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user= authenticate(request,username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/')
                else:
                    messages.info(request,'Benutzerkonto ist nicht aktiv')
            else:
                messages.info(request,'Bitte überprüfe deine Login-Daten')

    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('/')
