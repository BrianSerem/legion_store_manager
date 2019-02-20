from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


from .managers import ProductQueryset


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    slug = models.SlugField(_("Slug"), max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


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

    objects = models.Manager()
    products = ProductQueryset.as_manager()

    class Meta:
        ordering = ("-name",)

    def __str__(self):
        return self.name
