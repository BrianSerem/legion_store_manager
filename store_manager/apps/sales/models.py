from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import ProductQueryset


class Category(models.Model):
    title = models.CharField(db_index=True, unique=True,max_length=200)
    category_description = models.CharField(blank=True,max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    """
    Product entity for the store.
    """
    name = models.CharField(_("Name"), max_length=255)
    category = models.ForeignKey("Category", related_name="products",
                                on_delete=models.CASCADE)
    description = models.TextField(_("Description"), blank=True)
    quantity = models.IntegerField(_("Quantity"))
    price = models.DecimalField(_("Price"),
                                decimal_places=2,
                                max_digits=12)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-name",)

    def __str__(self):
        return self.name
