from django.db import models
from django.utils import timezone
from django.contrib import admin
from uuid import uuid4
import json
from django.utils.html import escape
from django.core.exceptions import ValidationError

NULL = {"null": True, "blank": True}



class BaseModelMixin(models.Model):
    """
    Base Parent Model Mixin That Wraps All Common Fields and methods.
    child can override any of the methods or fields.
    """

    id = models.UUIDField(
        default=uuid4, primary_key=True, editable=False, db_index=True
    )

    created_at = models.DateTimeField(default=timezone.localtime)
    updated_at = models.DateTimeField(**NULL)

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self._state.adding:
            self.updated_at = timezone.localtime()
            self.clean_fields
        for f in self._meta.fields:
            raw_value = getattr(self, f.attname)
            if f.blank and raw_value in f.empty_values:
                continue
            elif type(raw_value) == str:
                try:
                    setattr(self, f.attname, escape(raw_value))
                except ValidationError as e:
                    pass
        super().save(*args, **kwargs)




