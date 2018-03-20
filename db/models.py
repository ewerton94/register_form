from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    course = models.CharField(max_length=250)
    semester = models.IntegerField()
    analytical_history = models.FileField(upload_to='analytical_histories')

    def __str__(self):
        return self.name
