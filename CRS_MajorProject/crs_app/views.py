import smtplib

from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.shortcuts import render, redirect, HttpResponseRedirect
from crs_app.models import *
from crs_app.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from CRS_MajorProject import settings as se

# Create your views here.
def crs_home_view(request):
    return render(request, "index.html")


def gov_schemes_view(request):
    return render(request, "governmentSchems.html")


@login_required()
def gov_jobs_view(request):
    jobs_list = GovernmentJobsModel.objects.all()
    main_title = 'Government Jobs'
    paginator = Paginator(jobs_list,1)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    my_dict = {"jobs_list": jobs_list, 'main_title': main_title,'post':post,'page':page}
    return render(request, "gov_jobs.html", context=my_dict)


@login_required()
def education_list_view(request):
    schemes_list = EducationModel.objects.all()
    main_title = 'Education and Learning'
    paginator = Paginator(schemes_list, 1)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    my_dict = {"schemes_list": schemes_list, 'main_title': main_title,'post':post,'page':page}
    return render(request, "schemes_list.html", context=my_dict)


@login_required()
def health_list_view(request):
    schemes_list = HealthModel.objects.all()
    main_title = 'Health and Wellness'
    paginator = Paginator(schemes_list, 1)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    my_dict = {"schemes_list": schemes_list, 'main_title': main_title, 'post': post, 'page': page}
    return render(request, "schemes_list.html", context=my_dict)


@login_required()
def agriculture_list_view(request):
    schemes_list = AgricultureModel.objects.all()
    main_title = 'Agriculture,Rural and Enviroment'
    paginator = Paginator(schemes_list, 1)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    my_dict = {"schemes_list": schemes_list, 'main_title': main_title, 'post': post, 'page': page}
    return render(request, "schemes_list.html", context=my_dict)


@login_required()
def electricity_list_view(request):
    schemes_list = ElectricityModel.objects.all()
    main_title = 'Electricity,Water and Local Services'
    paginator = Paginator(schemes_list, 1)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    my_dict = {"schemes_list": schemes_list, 'main_title': main_title, 'post': post, 'page': page}
    return render(request, "schemes_list.html", context=my_dict)


@login_required()
def business_list_view(request):
    schemes_list = BusinessModel.objects.all()
    main_title = 'Business and Self Employee'
    paginator = Paginator(schemes_list, 1)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    my_dict = {"schemes_list": schemes_list, 'main_title': main_title, 'post': post, 'page': page}
    return render(request, "schemes_list.html", context=my_dict)


@login_required()
def youth_list_view(request):
    schemes_list = YouthModel.objects.all()
    main_title = 'Youth and Sports'
    paginator = Paginator(schemes_list, 1)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    my_dict = {"schemes_list": schemes_list, 'main_title': main_title, 'post': post, 'page': page}
    return render(request, "schemes_list.html", context=my_dict)


def user_signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['first_name'].upper()
            lastname = form.cleaned_data['last_name'].upper()
            email = form.cleaned_data['email']
            user = form.save()
            user.set_password(user.password)
            user.save()
            subject = "Registration Confirmation Mail"
            user_message = "Hello,\n \"{} {}\" Thank You for registration".format(firstname,lastname )
            send_mail(subject, user_message, se.EMAIL_HOST_USER, [email])
            messages.success(request, 'Your Registration has been Successful.Thank you!')
            return HttpResponseRedirect('/accounts/login')
    my_dict = {'form': form}
    return render(request, "signup.html", context=my_dict)


def logout(request):
    return render(request, "logout_index.html")

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        user_email = request.POST.get("email")
        subject1 = request.POST.get("subject")
        message1 = request.POST.get("message")
        subject = "CRS"
        user_message = "Hello Mr. {} Thank You For Contact Us\n You are selected as junior java developer in Virim Info Tech Pvt.Ltd,Indore\nJoining Date:13/03/2021\nAnnual Salary: 3.5lpa\nJob Location:Indore".format(name)
        crs_message = "Sender Name: {}\n Email Id: {}:\n Subject: {}\n Message:{}".format(name,user_email,subject1,message1)
        crs_email = "crsinfo175@gmail.com"
        try:
            send_mail(subject,user_message, se.EMAIL_HOST_USER, [user_email])
            send_mail(subject1,crs_message, se.EMAIL_HOST_USER, [crs_email])
            messages.success(request, 'Your message has been sent. Thank you!')
            return HttpResponseRedirect('/')
        except smtplib.SMTPAuthenticationError:
            user_mess = EmailMessage(subject, user_message, se.EMAIL_HOST_USER, [user_email])
            crs_mess = EmailMessage(subject1, crs_message, se.EMAIL_HOST_USER, [crs_email])
            user_mess.send(fail_silently=True)
            crs_mess.send(fail_silently=True)
            return HttpResponseRedirect('/')

        # def send_mail(subject,message,from_email,recipient_list):
        # em = EmailMessage(subject, user_message, se.EMAIL_HOST_USER, [user_email])
        # try:
        #     mess = em.send(fail_silently=True)
        #     print(mess)
        # except smtplib.SMTPException as smtp:
        #     print(smtp)

