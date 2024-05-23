from django.db import models
from django.contrib.auth.models import User
from utils.base import BaseModelMixin
from django.contrib.auth.models import User


class CompPlan(models.Model):
    Flat_Fee             = models.FloatField(default=0)
    Percentage           = models.FloatField()
    Minimum_Compensation = models.FloatField(default=2.75)
    Maximum_Compensation = models.FloatField(default=2750)
    MAX_GCI              = models.FloatField(default=27500)
    FF_MIN_LOAN          = models.IntegerField(default=27500)
    
    def __str__(self) -> str:
        return f"{self.Percentage}"
    
    # def save(self):
    #     return 
    
    
class Bps(models.Model):
    """
		Table that store bps information interval and maxmium value
    """
    bps       = models.FloatField(default=275)
    interval  = models.IntegerField(default=50)
    max_value = models.FloatField()
    
    def __str__(self):
        return f"{self.bps}"
    
    
class LoanBreakPoint(models.Model):
    loan_break_point = models.FloatField(default=1000000)
   

    def __str__(self):
        return f"{self.loan_break_point}"
    
    
class AHF(models.Model):
    commission = models.FloatField()
    loan_per_year = models.IntegerField(default=1)
    loan_per_month = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.commission}"
    
    
class Branch(models.Model):
    commission = models.DecimalField(max_digits=10,decimal_places=2,default=0.7)
    loan_per_year = models.IntegerField(blank=True,null=True)
    loan_per_month = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.commission}"
    
    
    
    
    
    
class Loan(models.Model):
	user = models.ForeignKey(User,blank= True,null=True,on_delete= models.CASCADE)
	amount = models.FloatField()

	def __str__(self):
 		return self.amount



class Company(models.Model):
    name = models.CharField(max_length = 1000,blank=True,null=True)
    cap = models.FloatField()
    company_commission = models.FloatField()
    number_of_loans = models.IntegerField(blank = True,null = True)
    total = models.FloatField()
    def __str__(self):
        return self.name

 
class Recruiter(models.Model):
    name  = models.CharField(max_length=100,null=True,blank=True)
    level = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class MLO(models.Model):
	"""
 
	a MLO in order to count they must averge 1 in month.

		they have to close deals one loan in month.
		in order to count to tier person has to do 12 deals per year
		4 loans in 4th month averge will be 1 that will count
		4 loans in 5th they don't count

	   say person on level 1 june to may 

	"""
 
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	level = models.IntegerField(max_length=1)
	# name = models.CharField(max_length = 100,blank = True,null = True)
	# NMLS_ID = models.IntegerField(blank = True,null = True)
	# NMLS_sponsor_id = models.IntegerField(blank = True,null = True)
	# MLO_commision  = models.FloatField(blank = True,null = True)
	# annual_commision_paid_to_company  = models.IntegerField(blank = True,null = True)
	# comp = models.FloatField(blank = True,null=True)
	# gci = models.FloatField(blank = True,null=True)
	# date_joined = models.DateTimeField(auto_now = True)
	# break_point  =   models.FloatField(blank = True,null=True)
	