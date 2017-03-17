import uuid

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse_lazy


def generate_image_name(instance, filename):
    url = "image_{}_{}".format(instance.user.username, uuid.uuid4())
    return url


class Item(models.Model):
    user = models.ForeignKey(User)
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200,
                                   verbose_name='Short Description')
    details = models.CharField(max_length=600, verbose_name='Details')
    price = models.IntegerField(validators=[MinValueValidator(0)])
    delivery_date = models.DateField(verbose_name='Expected Delivery Date')
    other_features = models.CharField(max_length=600, blank=True, null=True)
    image1 = models.ImageField(upload_to=generate_image_name)
    image2 = models.ImageField(upload_to=generate_image_name, blank=True,
                               null=True)
    image3 = models.ImageField(upload_to=generate_image_name, blank=True,
                               null=True)
    image4 = models.ImageField(upload_to=generate_image_name, blank=True,
                               null=True)

    def get_absolute_url(self):
        return reverse_lazy('item-detail', args=[str(self.pk)])

    def __str__(self):
        return self.product_name
