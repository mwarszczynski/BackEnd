from django.db import models


class Producer(models.Model):                           # Toyota
    model = models.CharField(max_length=250)            # Corolla
    model_enginee = models.CharField(max_length=500)    # fuel/oil/diesel
    color = models.CharField(max_length=100)            # color
    model_logo = models.CharField(max_length=1000)      # model logo/string

    def __repr__(self):
        return self.model + ' - ' + self.model_enginee


class Brand(models.Model):                                                  # Marka
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)        # relacja - producent
    file_type = models.CharField(max_length=10)                             # 
    
