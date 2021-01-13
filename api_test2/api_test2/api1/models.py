from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)

    __str__ = __repr__