from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

class Note(ExportModelOperationsMixin('note') ,models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    label = models.TextField(null=False, blank=True, max_length=255)
    text = models.TextField(null=False, blank=True)
    archived = models.BooleanField(default=False)