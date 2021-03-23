from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def advert(request):
    if request.method == "POST":
        return redirect('post:home')
    return render(request, "advert/ad_content.html")