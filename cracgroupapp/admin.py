from django.contrib import admin
from cracgroupapp import models

# Register your models here.
admin.site.register(models.PaymentModel)
admin.site.register(models.ProductDonationModel)
admin.site.register(models.VolounteerModel)

