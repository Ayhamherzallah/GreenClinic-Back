from django.db import models

class Appointment(models.Model):
    client_name = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.client_name


class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    profile_image = models.ImageField(null=True, blank=True)
    service = models.CharField(max_length=255, null=True, blank=True)
    review = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.client_name} - {self.rating} "


class BeforeAfterSwiper(models.Model):
    before_image = models.ImageField(null=True, blank=True)
    after_image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
