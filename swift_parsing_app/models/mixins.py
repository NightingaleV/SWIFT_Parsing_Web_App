from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class CreationModificationDateMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(_('creation date and time'), auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(_('modification date and time'), auto_now=True, blank=True)