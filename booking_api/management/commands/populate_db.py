from django.core.management.base import BaseCommand
from booking_api.models import *

class Command(BaseCommand):

    def _create_sites(self):
        site_obj = Site.objects.get(id=1)
        site_types = ['Tent', 'Pull Through', 'Back In']

        for i in range(15):
            for type in site_types:
                site_obj.id = None
                site_obj._state.adding = True
                site_obj.site_type = type

                site_obj.save()
                print("Created Site Object")
        

    def handle(self, *args, **options):
        self._create_sites()