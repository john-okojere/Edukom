from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('Get_a_tutor', views.get_a_tutor, name="GetATutor"),
    path('FAQs', views.faq, name="faq"),
    path('succes_form/<uuid:uid>/', views.succes_form, name="succes_form"),
    ]
