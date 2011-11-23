from django.db import models

class BookManager(models.Manager):
    """
    Book Manager
    """
    # use for related fields
    use_for_related_fields = True

    def get_old_testament(self):
        return self.get_query_set().filter(is_new_testament=False)

    def get_new_testament(self):
        return self.get_query_set().filter(is_new_testament=True)

