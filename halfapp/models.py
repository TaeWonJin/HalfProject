from django.db import models

class Account(models.Model):
    CHOICES=(
        ('New','신규'),
        ('Work','출근'),
        ('NotWork','결근'),
    )
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=50)
    youwork = models.CharField(max_length=20,choices=CHOICES,default='New')

    def __str__(self):
        return self.name

class Workrecode(models.Model):
    name = models.CharField(max_length=20)
    youwork = models.CharField(max_length =20)
    pub_date =models.DateTimeField('date published')