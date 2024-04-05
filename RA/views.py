from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import member
# import mysql.connector as sql
user_n=''
eml=''
pswd=''


def Home(request):
    return render(request, 'index.html')

def Login(request):
    return render(request, 'login.html')

def About(request):
    return render(request, 'about.html')

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

def Signup(request):
    global user_n,eml,pswd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="1002",database="RentalAxis")
        mycursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="username":
                user_n=value
            elif key=="email":
                eml=value
            elif key=="password":
                pswd=value

        # c=insert(INSERT into USERS values('{}','{}',{});.format(user_n,eml,pswd))

def users(request):
  users = member.objects.all().values()
  template = loader.get_template('users_list.html')
  context = {
    'users': users,
  }
  return HttpResponse(template.render(context, request))

    # Creates a mymembers object with all the values of the Member model.
    # Loads the all_members.html template.
    # Creates an object containing the mymembers object.
    # Sends the object to the template.
    # Outputs the HTML that is rendered by the template.


def details(request, id):
  users = member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'users': users,
  }
  return HttpResponse(template.render(context, request))

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))