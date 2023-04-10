from django.db import models

class Customer(models.Model):
    class Meta:
        db_table = 'customer'

    name = models.CharField(max_length=100, null=False)
    street = models.CharField(max_length=50, null=True, blank=True, default='')
    city = models.CharField(max_length=50, null=True, blank=True, default='')
    state = models.CharField(max_length=2, null=True, blank=True, default='')
    zip_code = models.CharField(max_length=5, null=True, blank=True, default='')
    contact_name = models.CharField(max_length=50, null=True, blank=True, default='')
    contact_phone = models.CharField(max_length=50, null=True, blank=True, default='')

    def __str__(self):
        return f'{self.name}'

