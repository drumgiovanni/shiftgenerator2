from django.db import models

# Create your models here.
class Workers(models.Model):
    worker_name = models.CharField(max_length = 95, unique=True)
    worker_fname = models.CharField(max_length= 95, unique=True)
    w_num = models.CharField(max_length= 23, unique=True)
    mail = models.CharField(max_length=95, unique=True)

    def values(self):
    	return self.worker_name, self.worker_fname, self.w_num, self.mail

    def __str__(self):
    	return self.worker_name