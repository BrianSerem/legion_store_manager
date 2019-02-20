from django.db.models.query import QuerySet


class ProductQueryset(QuerySet):

    def active(self):
        return self.filter(deleted=False)
