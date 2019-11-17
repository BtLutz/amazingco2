from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class TreeNode(MPTTModel):
    parent = TreeForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        db_index=True,
        on_delete=models.CASCADE,
    )
    root = TreeForeignKey(
        "self", on_delete=models.DO_NOTHING, null=True, blank=True, editable=False
    )
    is_root = models.BooleanField(default=False, editable=False)
