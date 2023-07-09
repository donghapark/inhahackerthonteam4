from django.db import models

# Create your models here.


# 성인ADHD, 분노조절장애, 알코올중독, 우울증 

class mental_illness(models.Model):
    name = models.CharField(max_length=300)
    count1 = models.FloatField()
    count2 = models.FloatField()
    count3 = models.FloatField()
    count4 = models.FloatField()
    count5 = models.FloatField()
    def __str__(self):
        return self.name
