from django.core.management.base import BaseCommand
from core.models import Items  # Adjust 'yourapp' to your actual app name
from django.db import transaction

class Command(BaseCommand):
    help = 'Remove duplicate Items based on title'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting duplicate removal...")

        # Step 1: Identify duplicates
        title_dict = {}
        for item in Items.objects.all():
            if item.title in title_dict:
                title_dict[item.title].append(item)
            else:
                title_dict[item.title] = [item]

        # Step 2: Remove duplicates
        total_deleted = 0
        with transaction.atomic():
            for items in title_dict.values():
                if len(items) > 1:
                    # Keep the first item, delete the rest
                    to_keep = items[0]
                    to_delete = items[1:]

                    for item in to_delete:
                        item.delete()
                        total_deleted += 1
                        self.stdout.write(f"Deleted: {item}")

        self.stdout.write(f"Duplicate removal complete. {total_deleted} items deleted.")
