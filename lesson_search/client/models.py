from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Продукт кредитования')
    interest_rate = models.FloatField(verbose_name='Процентная ставка', default=28)
    max_sum = models.IntegerField(verbose_name='Сумма 1', default=100000)
    commission = models.FloatField(verbose_name='Комиссия за выдачу', default=0)

    def __str__(self):
        return self.product_name


class Customer(models.Model):
    name = models.CharField(max_length=50)
    request_date = models.DateField()
    birth_date = models.DateField()
    sum = models.IntegerField()
    STATUS_CHOICES = (
        (1,'На рассмотрении'),
        (2,'Одобрен'),
        (3,'Отказано')
    )
    status = models.IntegerField(choices=STATUS_CHOICES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

