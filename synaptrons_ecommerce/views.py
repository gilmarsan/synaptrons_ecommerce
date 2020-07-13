from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django .shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        "title": "Página principal",
        "content": "Bem-vindo à Página Principal"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "Página sobre",
        "content": "Bem-vindo à página sobre"
    }
    return render(request, "about/view.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Página de contato",
        "content": "Bem-vindo à página de contato",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)
