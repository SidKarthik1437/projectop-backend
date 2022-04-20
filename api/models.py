from django.db import models
# Create your models here.

states = (("created", "created"),
          ("in_progress", "in_progress"),
          ("completed", "completed"),
          ("failed", "failed"))


class Prob(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    location = models.JSONField(blank=False, null=False)
    state = models.TextField(max_length=20, blank=False,
                             null=False, default='created', choices=states)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
