from django.urls import path
from . import views

urlpatterns = [
    path('appointment/', views.appointment_list),
    path('appointment/<int:pk>/', views.appointment_detail),

    path('testimonial/', views.testimonial_list),
    path('testimonial/<int:pk>/', views.testimonial_detail),

    path('swiper/', views.beforeafterswiper_list),
    path('swiper/<int:pk>/', views.beforeafterswiper_detail)
]