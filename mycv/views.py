from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .models import Comment, genericPWD

from .forms import GuestCommentForm, PasswordInputValue, MailForm


def setcookie(request, html):
    if request.COOKIES.get('visits'):
        html.set_cookie('databack', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value +1)
    else:
        value=1
        html.set_cookie('visits', value, max_age=2592000)
        html.set_cookie('databack', 'Welcome for the first time', max_age=2592000)
    return html


def sendemail(request):
    template = loader.get_template('page/sendmassege.html')
    if request.method == 'GET':
        form = MailForm()
        context = {'form': form}
    if  request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            # emailAdress = request.POST.get('emailAdress')
            # subject = request.POST.get('subject')
            # bodyText = request.POST.get('bodyText')
            send_mail(
                "mail letter for test",
                "My first letter",
                "test@mewb.net",
                ["adovzhenok@ukr.net"],
            )
            form = MailForm()
            context = {'form': form}
    return HttpResponse(template.render(context=context, request=request))


def index(request):
    template = loader.get_template('page/index.html')
    indexpage=HttpResponse(template.render(request=request))
    return setcookie(request, indexpage)


def feedback(request):
    return render(request=request, template_name="page/feedback.html")


def createpassword(request):
    template = loader.get_template('page/password.html')
    if request.method == 'POST':
        form = PasswordInputValue(request.POST)
        if form.is_valid():
            input1 = request.POST.get('namberCount', 1)
            input2 = request.POST.get('passwordLen', 8)
            passwords = genericPWD(input1, input2).layoutpwd()
            form = PasswordInputValue(initial={'namberCount': input1, 'passwordLen': input2})
            context = {'passwords': passwords, 'form': form}
            return HttpResponse(template.render(context=context, request=request))
        else:
            messages.add_message(request, messages.INFO, "Please check input data")
    form = PasswordInputValue()
    context = {'form':form}
    return HttpResponse(template.render(context=context,  request=request))


def saveComment(request):
    feedbackoutput = Comment.objects.all()
    template = loader.get_template('page/contacts.html')
    if request.method == 'POST':
        fbk = GuestCommentForm(request.POST)
        if fbk.is_valid():
            fbk.save()
            messages.add_message(request, messages.INFO, "Ваше повідомлення добавлене")
            return redirect('index')
        else:
            messages.error(request, 'Please check captcha and email')
    else:
        fbk = GuestCommentForm()
    context = {'form': fbk, 'feedbackoutput':feedbackoutput}
    return HttpResponse(template.render(context=context,  request=request))


# sender = 'adovzhenok@ukr.net'
# recipients = ['admin@bikemaps.org','tech-support@bikemaps.org']
# email = EmailMessage(subject='Test', body='Test', 'admin@bikemaps.org', recipients, headers = {'Reply-To': sender})
# email.send()