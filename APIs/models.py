from django.db import models

# Create your models here.


class New(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class CompanyImg(models.Model):

    name = models.CharField(max_length=60, null=True)
    coImg = models.ImageField(upload_to='companyImg', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name