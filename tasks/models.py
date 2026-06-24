from django.db import models

class Task(models.Model):

    title = models.CharField(max_length=255)
    task_status=models.BooleanField(default=False)
    task_created_at=models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.title