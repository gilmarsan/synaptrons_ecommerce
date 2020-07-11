from django.http import HttpResponse
from django .shortcuts import render
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
    context = {
        "title": "Página de contato",
        "content": "Bem-vindo à página de contato"
    }
    return render(request, "about/view.html", context)
