from django.db.models import QuerySet


class ProductQueryset(QuerySet):

    def active(self):
        return self.filter(deleted=False)
