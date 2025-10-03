from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Chat, Mensaje
from .forms import MensajeForm
# Create your views here.

'''
Mostrar la lista de todos los chats del usuario
'''
@login_required
def chat_list(request):
    #chats = Chat.objects.filter(usuario_emisor=request.user) | Chat.objects.filter(usuario_receptor=request.user)
    #usuarios = User.objects.exclude(id=request.user.id)
    #return render(request, "mensajeria/chat_list.html", {"chats": chats, "usuarios": usuarios})

    usuarios = User.objects.exclude(id=request.user.id)
    chats = Chat.objects.filter(usuario_emisor=request.user) | Chat.objects.filter(usuario_receptor=request.user)
    for chat in chats:
        chat.otro_usuario = chat.usuario_receptor if chat.usuario_emisor == request.user else chat.usuario_emisor
    return render(request, "mensajeria/chat_list.html", {"chats": chats, "usuarios": usuarios})

''' 
Mostrar los mensajes de un chat específico y permitir enviar nuevos mensajes
'''
@login_required
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    # verificar que el usuario actual es parte del chat
    if request.user not in [chat.usuario_emisor, chat.usuario_receptor]:
        return redirect("mensajeria:chat_list")

    mensajes = chat.mensajes.all()

    # Marcar los mensajes del otro usuario como leídos
    mensajes.exclude(usuario_remitente=request.user).filter(leido=False).update(leido=True)

    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            nuevo_mensaje = form.save(commit=False)
            nuevo_mensaje.chat = chat
            nuevo_mensaje.usuario_remitente = request.user
            nuevo_mensaje.save()
            return redirect("mensajeria:chat_detail", chat_id=chat.id)
    else:
        form = MensajeForm()

    return render(request, "mensajeria/chat_detail.html", {
        "chat": chat,
        "mensajes": mensajes,
        "form": form
    })

'''
Crear un nuevo chat entre el usuario actual y otro usuario
'''
@login_required
def chat_create(request, user_id):
    receptor = get_object_or_404(User, id=user_id)
    chat, creado = Chat.objects.get_or_create(
        usuario_emisor=request.user, usuario_receptor=receptor
    )
    return redirect("mensajeria:chat_detail", chat_id=chat.id)
