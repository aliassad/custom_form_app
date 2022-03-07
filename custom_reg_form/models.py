from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    """
    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.SET_NULL)
    FAVORITE_EDITOR = (
        ('vim', 'Vim'),
        ('emacs', 'Emacs'),
        ('np', 'NotePad'),
        ('cat', 'cat > filename'),
    )

    favorite_movie = models.CharField(
        verbose_name="Fav Movie",
        max_length=100
    )
    favorite_editor = models.CharField(
        verbose_name="Favorite Editor",
        choices=FAVORITE_EDITOR,
        max_length=100
    )
