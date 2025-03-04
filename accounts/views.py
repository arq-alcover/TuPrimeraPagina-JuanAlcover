from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserProfileForm, CustomUserCreationForm
from .models import UserProfile
from django.conf import settings

# ✅ Vista para iniciar sesión
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("post_list")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

# ✅ Vista para cerrar sesión
def logout_view(request):
    logout(request)
    return redirect("post_list")

# ✅ Vista para registrarse con el formulario personalizado
def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            # Se crea el perfil automáticamente al registrarse
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect("post_list")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})

# ✅ Vista para ver el perfil de usuario
@login_required
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, "accounts/profile.html", {
        "user_profile": user_profile,  
        "MEDIA_URL": settings.MEDIA_URL  
        })

# ✅ Vista para editar el perfil de usuario, incluyendo imagen
@login_required
def profile_edit_view(request):
    user_profile = request.user.profile

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, "accounts/profile_edit.html", {"form": form})
