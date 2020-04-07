from .models import JointDonationModel


# def AddToDonation(amount, product):
#     '''
#     this function helps to add users in a joint donation and also increase the donation progress
#     '''
#     product_obj                              = JointDonationModel.objects.get(product=product)
#     product_obj.donation_count              += 1
#     product_obj.donated_amount              += amount
#     unit_price                              = product_obj.unit_price
#     product_obj.donation_circle             = product_obj.donated_amount//unit_price
#     product_obj.ongoing_circle_count        = product_obj.donated_amount%unit_price
#     product_obj.save()
    
#     return product_obj


