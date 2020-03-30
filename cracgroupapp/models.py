from django.db import models


class VolounteerModel(models.Model):
    '''
    holds information of the registered volounteers
    '''
    name                = models.CharField( max_length=100, blank=False, null=True)
    email               = models.EmailField(max_length=254, unique=True)
    phone_number        = models.CharField( max_length=50, blank=True, null=True)
    gender              = models.CharField( max_length=50, null=True, blank=True)
    address             = models.CharField(max_length=255, null=True, blank=True)
    organization_name   = models.CharField(max_length=255, null=True, blank=True)
    is_charity_org      = models.BooleanField(default=False)
    is_logistic_company = models.BooleanField(default=False)


class PaymentModel(models.Model):
    '''
    holds information on all successful payments made on the platform
    '''
    fullname            = models.CharField( max_length=250, null=True, blank=True)
    email               = models.CharField(max_length=100, null=True, blank=True)
    txnstatus           = models.CharField(max_length=50, null=True, blank=True)
    txnref              = models.CharField(max_length=250, null=True, blank=True)
    bankmessage         = models.CharField( max_length=250, null=True, blank=True)
    paymentmethod       = models.CharField( max_length=50, null=True, blank=True)
    amount              = models.CharField( max_length=250, null=True, blank=True)
    message             = models.CharField( max_length=250, null=True, blank=True)
    fraudstatus         = models.CharField( max_length=50, null=True, blank=True)


