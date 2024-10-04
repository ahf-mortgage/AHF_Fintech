from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import Bps,CompPlan,LoanBreakPoint
import random

class Command(BaseCommand):
    help = 'update users from a text file'

    def handle(self, *args, **options):
        all_users = User.objects.all()
        for user in all_users:
            loan_break_point = LoanBreakPoint.objects.create(user = user)
            print("loan_break_point = ",loan_break_point)
