from django.db import models
from django.conf import settings
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

class TimeStamped(models.Model):
    """
    Creation time and update timestamps
    """
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Sale(TimeStamped):
    """This class defines a sale instance"""
    attendant = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)


class SaleItem(models.Model):
    sale = models.ForeignKey('Sale', related_name="sale_items",
                            on_delete=models.CASCADE)
    product = models.ForeignKey('Product', related_name="sale_items",
                               on_delete=models.CASCADE)
    product_title = models.CharField(_("Product Title"), max_length=255)
    quantity = models.IntegerField(_("Quantity"))

    def __str__(self):
        return "Product: {}, Quantity: {}".format(self.product_title, self.quantity)
