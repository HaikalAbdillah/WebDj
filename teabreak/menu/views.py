from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'nama' : 'ini cuman bikin pusing dan capek tapi insha allah lillah',
    }
    return render(request, 'index.html', context)