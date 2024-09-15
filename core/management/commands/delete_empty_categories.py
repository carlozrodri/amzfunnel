from django.core.management.base import BaseCommand
from core.models import Categorias, Items

class Command(BaseCommand):
    help = 'Delete categories with no associated items'

    def handle(self, *args, **kwargs):
        # Query to find categories with no associated items
        empty_categories = Categorias.objects.filter(items__isnull=True)

        if empty_categories.exists():
            # Count the number of categories to be deleted
            count = empty_categories.count()
            empty_categories.delete()
            
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} categories with no items.'))
        else:
            self.stdout.write(self.style.WARNING('No empty categories found to delete.'))
