from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.http import JsonResponse
from .models import VolounteerModel, PaymentModel

from .forms import ContactForm

def home(request):
    return render(request, 'index.html')


def ContactFormSubmitView(request):
    if request.method == 'POST':
        
        contact_name            = request.POST['contactName']
        contact_email           = request.POST['contactEmail']
        contact_message         = request.POST['contactName']
        contact_phone_number    = request.POST['contactMessage']

        template                = get_template('email_template/contact_template.txt')
        params                  = {
                                    'contact_name': contact_name,
                                    'contact_email': contact_email,
                                    'contact_message': contact_message,
                                    'contact_phone_number': contact_phone_number,
                                    }
        content                 = template.render(params)

        email                   = EmailMessage(
                                    subject     = "New contact Email on CRAC GROUP",
                                    from_email  = contact_email,
                                    to          = ['demo@email.com'],
                                    body=content,
                                )
        email.send()

        data = {
            "message": 'your message has been sent we would contact you soon',
        }
        
        return JsonResponse(data)


def VolounteerView(request):
    if request.method == 'POST':
        volounteer                      = request.POST['volounteer']
        volounteer_name                 = request.POST['volounteerName']
        volounteer_email                = request.POST['volounteerEmail']
        volounteer_phone_number         = request.POST['volounteerPhoneNumber']
        volounteer_gender               = request.POST['volounteerGender']
        volounteer_address              = request.POST['volounteerAddress']
        volounteer_organization_name    = request.POST['volounteerOrganizationName']
        # vehicle_ownership               = request.POST['vehicleOwnership']
        
        if volounteer == 'logistic':
            VolounteerModel.objects.create(name=volounteer_name, email=volounteer_email, phone_number=volounteer_phone_number, gender=volounteer_gender, address=volounteer_address, organization_name=volounteer_organization_name, is_logistic_company=True)
        else:
            VolounteerModel.objects.create(name=volounteer_name, email=volounteer_email, phone_number=volounteer_phone_number, gender=volounteer_gender, address=volounteer_address, organization_name=volounteer_organization_name, is_charity_org=True)

        data = {
            "message": 'thank you for volounteering, you would recieve a message from us',
        }

    return JsonResponse(data)


def PaymentView(request):
    if request.method == 'POST':
        fullname            = request.POST['response[fullname]']
        email               = request.POST['response[email]']
        txnstatus           = request.POST['response[txnStatus]']
        txnref              = request.POST['response[txnRef]']
        bankmessage         = request.POST['response[bank_message]']
        paymentmethod       = request.POST['response[payment_method]']
        amount              = request.POST['response[chargedAmount]']
        message             = request.POST['response[message]']
        fraudstatus         = request.POST['response[fraudStatus]']

        PaymentModel.objects.create(fullname=fullname, email=email, txnstatus=txnstatus, txnref=txnref, bankmessage=bankmessage, paymentmethod=paymentmethod, amount=amount, message=message, fraudstatus=fraudstatus)

        data = {
            "message": 'thank you for volounteering, you would recieve a message from us',
        }

    return JsonResponse(data)