from django.conf.urls import url
from cracgroupapp import views


urlpatterns = [
    url(r"^contactformsubmit/$", views.ContactFormSubmitView, name="contactformsubmit"),
    url(r"^VolounteerRegistration/$", views.VolounteerView, name="volounteer_reg"),
    url(r"^Payment/$", views.PaymentView, name="payment"),
    url(r"^ProductDonation/$", views.ProductDonationView, name="product-donation"),
    url(r"^one-time-donation/$", views.DimOneTimeDonationView, name="one-time-donation"),
    url(r"^10WeeksDonation/$", views.DimReocurringDonationView, name="reoccuring-diim"),
    url(r"^matching-donations-1m/$", views.MatchingDonation1MView, name="matching-donation-1m"),
    url(r"^matching-donations-5m/$", views.MatchingDonation5MView, name="matching-donation-5m"),
    url(r"^matching-donations-20m/$", views.MatchingDonation20MView, name="matching-donation-20m"),
    
]
