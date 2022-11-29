from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    
    def __str__(self):
        return self.user

    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name', 'last_name', 'email', 'password', 'role')

