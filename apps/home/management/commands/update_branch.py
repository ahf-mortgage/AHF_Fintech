from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import Bps,CompPlan,LoanBreakPoint,Branch
import random

class Command(BaseCommand):
    help = 'update users from a text file'

    def handle(self, *args, **options):
        branches = Branch.objects.all()
        for branch in branches:
            branch.loan_per_month = 1
            branch.loan_per_year = 12
            branch.save()
            print("branch = ",branch)
