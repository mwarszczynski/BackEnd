from django.db import models


class Producer(models.Model):
    model = models.Charfield(max_length=250)
    model_enginee = models.Charfield(max_length=500)
    color = models.Charfield(max_length=100)
    model_logo = models.Charfield(max_length=1000)


class Brand(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    file_type = models.Charfield(max_length=10)
    
