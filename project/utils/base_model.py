from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()


class SoftDeletedQuerySet(models.QuerySet):

    def get_queryset(self):
        return self.filter(deleted__isnull=False)


class BaseModel(models.Model):
    """ Basic models fields """

    stored = SoftDeletedQuerySet.as_manager()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    deleted = models.DateTimeField(null=True)
    deleted_by = models.ForeignKey(
        USER, null=True, on_delete=models.PROTECT,
        related_name='+'
    )

    class Meta:
        abstract = True
