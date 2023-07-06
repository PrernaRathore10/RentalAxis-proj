from django.shortcuts import render

def Home(request):
    return render(request, 'index.html')

def Login(request):
    return render(request, 'login.html')

def Register_rent(request):
    return render(request, 'register_rent.html')

def Register_sell(request):
    return render(request, 'register_sell.html')
    
def Donation(request):
    return render(request, 'donation.html')

def Chatbot(request):
    return render(request, 'bot.html')

def Contact(request):  
    return render('Contact us')