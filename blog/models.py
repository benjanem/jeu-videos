from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    # Date de sortie
    published_date = models.DateTimeField(blank=True, null=True)

    # Image de couverture du jeu vidéo
    image = models.URLField(null=True, blank=True)

    # Nombre d'exemplaires vendus
    sold_amount = models.CharField(max_length=200, blank=True, null=True)

    video = models.CharField(max_length=200, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
