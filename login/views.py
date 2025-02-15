from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect("home")  # Redirige vers la page d'accueil
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, "auth/login.html")

def user_logout(request):
    logout(request)
    messages.success(request, "Déconnexion réussie.")
    return redirect("login")  # Redirige vers la page de connexion
