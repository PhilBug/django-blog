from django.shortcuts import render
from posts.models import Post
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (From, To, PlainTextContent, Mail)
from os import environ


def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact_form.html')


def sendmail(request):
    sendgrid_client = SendGridAPIClient(
        api_key=environ.get('SENDGRID_API_KEY'))
    from_email = From(environ.get('ADMIN_EMAIL'))
    to_email = To(environ.get('ADMIN_EMAIL'))
    subject = request.POST['fname'] + ' ' + \
        request.POST['lname'] + ' - phone num: ' + request.POST['phone']
    plain_text_content = PlainTextContent(
        request.POST['message']
    )
    message = Mail(from_email, to_email, subject, plain_text_content)
    response = sendgrid_client.send(message=message)
    print(response)

    return render(request, 'pages/contact_form.html', {'email_sent': True})
