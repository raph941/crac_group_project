from .models import JointDonationModel, JointDonatorModel


def AddToDonation(fullname, amount, product):
    '''
    this function helps to add users in a joint donation and also increase the donation progress
    '''
    JointDonatorModel.objects.create(fullname=fullname, amount=amount)
    donator                 = JointDonatorModel.objects.get(fullname=fullname, amount=amount)
    product_obj             = JointDonationModel.objects.get(product=product)
    product_obj.donators.add(donator)
    product_obj.donation_count += 1
    product_obj.donated_amount += amount
    unit_price              = product_obj.unit_price
    circle_count            = product_obj.donated_amount//unit_price
    product_obj.donation_circle = circle_count
    product_obj.save()
    
    return product_obj