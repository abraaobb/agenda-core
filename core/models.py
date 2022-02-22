from django.db import models

# Create your models here.


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name=('Created at')
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True,
        blank=True,
        verbose_name=('Modified at')
    )
    is_active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True,
        verbose_name=('Active')
    )

    class Meta:
        abstract = True


class Contact(ModelBase):
    class Category(models.TextChoices):
        FAMILY = '0', ('Family')
        FRIEND = '1', ('Friend')
        OTHER = '2', ('Other')

    name = models.CharField(
        db_column='tx_name',
        max_length=128,
        null=False,
        blank=False,
        verbose_name=('Name')
    )
    phone = models.CharField(
        db_column='tx_phone',
        max_length=32,
        null=False,
        blank=False,
        verbose_name=('Phone')
    )
    category = models.CharField(
        max_length=2,
        db_column='cs_category',
        null=False,
        blank=False,
        choices=Category.choices,
        default=Category.FAMILY,
        verbose_name=('Category')
    )

    class Meta:
        managed = True
        db_table = 'contact'
        verbose_name = ('Contact')
        verbose_name_plural = ('Contacts')
