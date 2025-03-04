from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def message_list(request):
    """ Muestra los mensajes recibidos y enviados del usuario actual """
    messages_received = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    messages_sent = Message.objects.filter(sender=request.user).order_by('-timestamp')

    return render(request, "messaging/message_list.html", {
        "messages_received": messages_received,
        "messages_sent": messages_sent
    })

@login_required
def send_message(request):
    """ Permite al usuario enviar un mensaje a otro usuario """
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user 
            message.save()
            return redirect("message_list")  
    else:
        form = MessageForm()

    return render(request, "messaging/message_form.html", {"form": form})
