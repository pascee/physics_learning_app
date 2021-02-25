from django.db import models

class Drag_Object(models.Model):
    obj_name = models.CharField(max_length = 200)
    drag_coeficient = models.DecimalField(max_digits=10, decimal_places=3)