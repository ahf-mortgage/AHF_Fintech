from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT,Loan,LoanAmount
import random
import datetime

# Get the current date
today = datetime.date.today()

# Calculate the date from one year ago
one_year_ago = today.replace(year=today.year - 1)
commnads = [220,275,125]
class Command(BaseCommand):
    help = 'Creates mlo from a text file'
    def handle(self, *args, **options):
        loans = Loan.objects.all()
        index = 1
        for ln in loans:
            ln.bps = random.choice(commnads)
            ln.save()
