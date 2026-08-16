from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactoForm


def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu mensaje fue enviado. Te responderemos pronto.")
            return redirect("contacto:contacto")
    else:
        form = ContactoForm()

    return render(request, "contacto/contacto.html", {"form": form})