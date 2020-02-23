from django.core.mail import send_mail
from django.shortcuts import render
from atelier.forms import *
# Create your views here.

def index(request):
    return render(request , 'main_app/base.html')


# функція обробляє форму і надсилає на пошту
def home_page(request):
    # if request.method=='POST':
    #     form = EmailPostForms(request.POST)
    #     if form.is_valid():
    #         cd=form.cleaned_data
    #         #Тема
    #         subject= 'New message'
    #         message='Name {} \n\n  email : {}\n\n massage : {} '.format(cd['name'],cd['email'],
    #                                                                                     cd['message'])
    #         send_mail(subject,message,'admin@atelier.com',['vovasapuzhak2@gmail.com'])
    #         return render('Ok')
    #     else:
    #         form = EmailPostForms()
    #
    #         return index(request)
    # else:
        return render(request, 'main_app/home.html')



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
            #return request
            # return index(request)
