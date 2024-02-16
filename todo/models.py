from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=100)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'