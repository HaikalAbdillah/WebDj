from django.shortcuts import render

# Create your views here.

def contact(request):
    context = {
        'name' : 'ini infromasi lengkap kami',
    }
    return render(request, 'contact/contact.html', context)