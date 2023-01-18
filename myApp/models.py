from django.db import models

# Create your models here.

class Clan(models.Model):
    m_fname = models.CharField(max_length=20)
    m_lname = models.CharField(max_length=30)

    def __str__(self):
        return self.m_lname
