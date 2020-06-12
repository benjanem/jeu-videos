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
    image = models.ImageField(null=True, blank=True)

    # Nombre d'exemplaires vendus
    sold_amount = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Nombre d'exemplaires vendus",
        help_text="Nombre d'exemplaires vendus en millions"
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
