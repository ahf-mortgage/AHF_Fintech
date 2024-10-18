from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT,Loan,LoanAmount
import random
import datetime
from django.utils import timezone

# Get the current date
today = datetime.date.today()

# Calculate the date from one year ago
one_year_ago = today.replace(year=today.year - 1)



class Command(BaseCommand):
   
    help = 'Creates loan'
    def handle(self, *args, **options):

        number_loan = 1
        loans_amounts = [1000000,1000000,1000000]

        mlo_agents = MLO_AGENT.objects.all()
        mlo_id = 30903425
        index = 520

        today = datetime.datetime.today()

        for l in  Loan.objects.all():
            l.delete()

        for _ in range(number_loan):
            Loan.objects.create(bps = 2.75,)


        for agent in mlo_agents:
            for loan in Loan.objects.all():
                agent.loan = loan
                agent.save()
            

          
           
        # for  amount in LoanAmount.objects.all():
        #     for loan in Loan.objects.all():
        #         loan.amount.add(amount)
        #         loan.save()
                