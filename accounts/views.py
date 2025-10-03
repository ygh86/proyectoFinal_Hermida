from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import PerfilForm, UserRegisterForm
from .models import Profile

'''
Vistas para manejar el perfil del usuario y el registro.
'''
@login_required
def perfil(request):
    return render(request, "accounts/perfil.html", {"user": request.user})

'''
Vista para editar el perfil del usuario.
'''
@login_required
def editar_perfil(request):
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("accounts:perfil")
    else:
        form = PerfilForm(instance=request.user.profile)

    return render(request, "accounts/perfil_editar.html", {"form": form})

'''
Vista realizar un registro de usuario.
'''
def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Usuario creado correctamente! Ahora podés iniciar sesión.")
            return redirect("accounts:login")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/registro.html", {"form": form})
