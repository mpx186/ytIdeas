from django.db import models

IDEA_STATUS = (
    ('pending', 'waiting for review'),
    ('accepted', 'accepted'),
    ('done', 'done'),
    ('rejected', 'rejected')
)


# Create your models here.
class Idea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube_url = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=IDEA_STATUS, default='pending')


class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    reason = models.TextField()
