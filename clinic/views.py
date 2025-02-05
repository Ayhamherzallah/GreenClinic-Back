from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from . import models
from rest_framework.response import Response
from .serializers import AppointmentSerializer, TestimonialSerializer, BeforeAfterSwiperSerializer

@api_view(['GET','POST'])
def appointment_list(request):
    if request.method == 'GET':
        appointments= models.Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def appointment_detail(request,pk):

    try:
        appointment = models.Appointment.objects.get(pk = pk)
    except models.Appointment.DoesNotExist:
        return Response({"error": "Appointment Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AppointmentSerializer(appointment, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def testimonial_list(request):
    if request.method == 'GET':
        testimonials = models.Testimonial.objects.all()
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TestimonialSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def testimonial_detail(request, pk):

    try:
        testimonial = models.Testimonial.objects.get(pk = pk)
    except models.Testimonial.DoesNotExist:
        return Response({"error": "Testimonial Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TestimonialSerializer(testimonial)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TestimonialSerializer(testimonial,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        testimonial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['Get','POST'])
def beforeafterswiper_list(request):
    if request.method == 'GET':
        swipers = models.BeforeAfterSwiper.objects.all()
        serializer = BeforeAfterSwiperSerializer(swipers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BeforeAfterSwiperSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def beforeafterswiper_detail(request, pk):

    try:
        swiper = models.BeforeAfterSwiper.objects.get(pk = pk)
    except models.BeforeAfterSwiper.DoesNotExist:
        return Response({"error": "swiper Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BeforeAfterSwiperSerializer(swiper)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BeforeAfterSwiperSerializer(swiper,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        swiper.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)