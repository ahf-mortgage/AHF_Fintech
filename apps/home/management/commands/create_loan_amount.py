from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT,Loan,LoanAmount
import random
import datetime

# Get the current date
today = datetime.date.today()

# Calculate the date from one year ago
one_year_ago = today.replace(year=today.year - 1)

class Command(BaseCommand):
    help = 'Creates mlo from a text file'
    def handle(self, *args, **options):
        loans = Loan.objects.all()
        amounts = LoanAmount.objects.all()
        i = 0

        for loan in loans:
            loan.amount.set(amounts)
            i += 1
            loan.save()
                