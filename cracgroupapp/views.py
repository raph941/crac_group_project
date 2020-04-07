from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.http import JsonResponse
from .models import VolounteerModel, PaymentModel, ProductDonationModel, JointDonationModel

from .forms import ContactForm

def home(request):
    products                        = JointDonationModel.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'index_temp.html', context)


def VolounteerView(request):
    if request.method == 'POST':
        volunteer_name                 = request.POST['volunteerName']
        volunteer_organization_name    = request.POST['volunteerOrganizationName']
        volunteer_email                = request.POST['volunteerEmail']
        volunteer_phone_number         = request.POST['volunteerPhoneNumber']
        volunteer_gender               = request.POST['volunteerGender']
        volunteer_address              = request.POST['volunteerAddress']
        volunteer_location             = request.POST['volunteerLocation']
        volunteer_address              = request.POST['volunteerAs']
        partner_as                     = request.POST['patrnerAs']
        
        
        VolounteerModel.objects.create(name=volunteer_name, email=volunteer_email, phone_number=volunteer_phone_number, gender=volunteer_gender, location=volunteer_location, address=volunteer_address, organization_name=volunteer_organization_name, volunteeras=volunteer_as, partner_as=partner_as)

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


def ProductDonationView(request):
    if request.method == 'POST':
        fullname                    = request.POST['fullname']
        email                       = request.POST['email']
        phone_number                = request.POST['phone_number']
        product_description         = request.POST['product_description']
        product_distribution        = request.POST['product_distribution']
        product                     = request.POST['product']
        pickup_location             = request.POST['pickup_location']
        delivery_date               = request.POST['delivery_date']

        ProductDonationModel.objects.create(fullname=fullname, email=email, phone_number=phone_number, product=product, pickup_location=pickup_location, product_distribution=product_distribution, delivery_date=delivery_date, product_description=product_description)

    return render(request, 'product-donation.html')

def DimOneTimeDonationView(request):
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

    return render(request, 'one-time-donation.html')


def DimReocurringDonationView(request):
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

    return render(request, 'diim-donation-reocurring.html')


def MatchingDonation1MView(request):
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


    return render(request, 'matching-donation-1m.html')


def MatchingDonation5MView(request):
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


    return render(request, 'matching-donation-5m.html')


def MatchingDonation20MView(request):
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


    return render(request, 'matching-donation-20m.html')


def JointDonationView(request, pk):
    product = JointDonationModel.objects.get(pk=pk)
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

        product_pk          =  request.POST['product_id']
        product_obj         = JointDonationModel.objects.get(pk=product_pk)

        if txnstatus == 'successful':
            amount = int(float(amount))
            product_obj.donated_amount += amount
            product_obj.donation_count += 1

        product_obj.save()

    context = {
        'product': product
    }
    
    return render(request, 'joint-donation.html', context)


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