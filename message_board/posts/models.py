from cgitb import text
from xml.parsers.expat import model
from django.db import models

# Create your models here.
class Post(models.Model):
          text = models.TextField()
          
          def __str__(self):
                    return self.text[:50]
          