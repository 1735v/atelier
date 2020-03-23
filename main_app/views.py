from django.core.mail import send_mail
from django.shortcuts import render
from atelier.forms import *
from atelier.settings import *
# Create your views here.



google_api_url = "https://maps.googleapis.com/maps/api/js?key={}&callback=initMap".format(GOOGLE_API_KEY)



def index(request):
    return render(request , 'main_app/base.html')



def home_page(request):

        return render(request, 'main_app/home.html',{"google_api_url":google_api_url})


# функція обробляє форму і надсилає на пошту
def send_forms_for_email(request):
    if request.method == 'POST':
        form = EmailPostForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Тема
            subject = 'New message'
            message = 'Name {} \n\n  email : {}\n\n massage : {} '.format(cd['name'], cd['email'],
                                                                          cd['message'])
            send_mail(subject, message, 'admin@atelier.com', ['vovasapuzhak2@gmail.com'])
            return index(request)
        else:
            form = EmailPostForms()

