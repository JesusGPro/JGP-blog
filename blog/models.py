from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):  # model.Model indica que Post es un modelo de django
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)  
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publishing_date = models.DateTimeField(blank=True, null=True)
    
    # ForeignKey es un link con otro modelo
    # CharField es un string limitando el numero de caracteres
    # TextField es un string sin limitacion  
    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
        
    def __str__(self):
        return self.title
        # obtenemos el texto de title
    
