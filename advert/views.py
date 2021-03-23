from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.

def advert(request):
    if request.method == "POST":
        return redirect('advert:ad_checkout')
    return render(request, "advert/ad_content.html")


def checkout(request):
    context = { "key":settings.STRIPE_PUBLISHABLE_KEY }
    if request.method == "POST":
        return render(request, "advert/successful_ad.html")
    return render(request, "advert/buy_ad.html", context)



def checked_out(request):
    if request.method=="POST":
        charge = stripe.Charge.create(
            amount=1000,
            currency="usd",
            description="Advert payment",
            source=request.POST['stripeToken']
        )
    return render(request, "advert/paid_ads.html")
    