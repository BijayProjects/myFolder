from django.urls import path
from .views import *

urlpatterns = [
    path('',Index.index, name='index'),
    path('about/',About1.about, name='about'),
    path('contact/',Contact.contact, name='contact'),
    path('product/',main_Product.product, name='product'),
    path('testimonial/',Testimonial.testimonial, name='testimonial'),
    path('client=signup/',ClientSignUP.client_signup, name='client_signup'),
    path('client=signin/',ClientSignIn.client_signin, name='client_signin'),
    path('feedback/',Customer_Feedbacks.feedback,name='feedbacks'),
     
]
