from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=100)
    count = models.IntegerField(default=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'

    def get_absolute_url(self):
        return reverse('products-list', args=[])