from django.db import models



class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True
        # No va a pertenecer a DB


class Classes (BaseModel):
    nombre = models.CharField(max_length=100)
