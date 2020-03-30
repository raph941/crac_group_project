from django.conf.urls import url
from cracgroupapp import views


urlpatterns = [
    url(r"^contactformsubmit/$", views.ContactFormSubmitView, name="contactformsubmit"),
    url(r"^VolounteerRegistration/$", views.VolounteerView, name="volounteer_reg"),
]