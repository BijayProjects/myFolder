from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('',views.SigIn.signin,name='signin'),
    path('SignUp/',views.SignUp.signup,name='signup'),

    path('signOut/',views.SignOut.signOut,name='signOut'),
    path('ordertable/',views.order_table ,name='order_table'),
    path('headline/',views.headline,name='headline'),
    path('about_meSections/',views.about_me , name='about_me_sections'),
    path('add-products/',views.add_products , name='add_products'),
    path('views-products/',views.view_products , name='view_products'),
    path('Testimonial_customer/',views.Customer_Testimonial,name='customer_testimonial'),
    path('customercontact/',views.Customer_Contact,name='customer_Contacts'),
    # add page function objects
    path('add-Headline/',views.Add_pages.add_headline, name='add_headline'),
    path('add-aboutME_contents/',views.Add_pages.add_about_content, name='add_about_content'),
    path('edit-products/<int:id>',views.Edits.edit_products, name='product_edit'),
    path('change_product_image/<int:id>',views.Edits.change_product_image, name='change_product_images'),
    path('edit_headline/<int:id>',views.Edits.edit_headline, name='edit_headline'),
    path('updateabout/<int:id>',views.Edits.update_about,name='update_about'),

    # All delete function
    path('delete_products/<int:id>',views.Product_delete, name='delete_product'),
    path('delete_headline/<int:id>',views.delete_headline, name='delete_headline'),
    path('delete_about/<int:id>',views.delete_about , name='delete_about'),


]
