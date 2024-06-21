from django.core.management.base import BaseCommand, CommandError
from apps.recruiter.models import Bps,LoanBreakPoint

class Command(BaseCommand):
    help = 'This is my command to init db'

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, help='Name of the object to create')

    def handle(self, *args, **options):
        name = options['name']
        if not name:
            pass
            # raise CommandError('You must provide a name for the object')

        obj = Bps.objects.create(bps=275)
        self.stdout.write(self.style.SUCCESS(f'Successfully created object: {obj.name}'))