from rest_framework import serializers
from .models import  Appointment, Testimonial, BeforeAfterSwiper

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class BeforeAfterSwiperSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeforeAfterSwiper
        fields = '__all__'