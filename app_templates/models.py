from django.db import models

# Create your models here.
class User1 (models.Model):
    f_nm = models.CharField(max_length=50)
    l_nm = models.CharField(max_length=50)
    u_email = models.EmailField()


    def __str__(self):
        return self.f_nm