from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.
class Article(models.Model):

    title = models.CharField(_("Title"), max_length=255)
    body = models.TextField(_("Article Body"))
    date = models.DateTimeField(_("Article Posted"), auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("articles")
        verbose_name_plural = _("articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles_detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("articles_list", kwargs={"pk": self.pk})
    