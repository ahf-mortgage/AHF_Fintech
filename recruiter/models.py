from django.db import models
from django.contrib.auth.models import User
from utils.base import BaseModelMixin
from django.contrib.auth.models import User


class CompPlan(models.Model):
    Flat_Fee = models.FloatField()
    Percentage = models.FloatField()
    Minimum_Compensation = models.FloatField()
    Maximum_Compensation = models.FloatField()
    MAX_GCI  = models.FloatField(blank=True,null=True)
    
    def __str__(self) -> str:
        return f"{self.Percentage}"
    
    
class Bps(models.Model):
    bps = models.FloatField()
    
    def __str__(self):
        return f"{self.bps}"
    
    
class LoanBreakPoint(models.Model):
    loan_break_point = models.FloatField()

    def __str__(self):
        return f"{self.loan_break_point}"
    
    
class AHF(models.Model):
    commission = models.FloatField()

    def __str__(self):
        return f"{self.commission}"
    
    
class Branch(models.Model):
    commission = models.DecimalField(max_digits=10,decimal_places=2)

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

 


class MLO(models.Model):
	"""
 
	a MLO in order to count they must averge 1 in month.

		they have to close deals one loan in month.
		in order to count to tier person has to do 12 deals per year
		4 loans in 4th month averge will be 1 that will count
		4 loans in 5th they don't count

	   say person on level 1 june to may 

	"""
 	# GROWTH_SHARE = [
	# 		'1':0,
	# 		'2':0.002,
	# 		'3':0.001,
	# 		'4':0.001,
	# 		'5':0.001,
	# 		'6':0.005,
	# 		'7':0.005

	# ]


	# HYPER_GROWTH_SHARE = [
	# 		'1':0.035,
	# 		'2':0.040
	# 		'3':0.025,
	# 		'4':0.015,
	# 		'5':0.010,
	# 		'6':0.025,
	# 		'7':0.005

	# ]
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	name = models.CharField(max_length = 100,blank = True,null = True)
	NMLS_ID = models.IntegerField(blank = True,null = True)
	NMLS_sponsor_id = models.IntegerField(blank = True,null = True)
	MLO_commision  = models.FloatField(blank = True,null = True)
	annual_commision_paid_to_company  = models.IntegerField(blank = True,null = True)
	comp = models.FloatField(blank = True,null=True)
	gci = models.FloatField(blank = True,null=True)

	date_joined = models.DateTimeField(auto_now = True)

	# for million of dollars
	break_point  =   models.FloatField(blank = True,null=True)
	# growth_share =   models.CharField(max_length = 10,choice =GROWTH_SHARE)
	# hyper_growth_share =   models.CharField(max_length = 10,choice =HYPER_GROWTH_SHARE)



	# def sponsor(self,sponsor_id_number):
	# 	self.NMLS_sponsor_id = sponsor_id_number
	# 	self.save()
	# 	return sponsor_id_number


	# def save(self):
	# 	cap = (0.25) * (2) * (10**6) # annual commission paid for company
	# 	if self.annual_production > cap:
	# 		cap = cap

	# 	self.MLO_commision = None

	# def __str__(self):
	# 	return f"{self.name}__{self.NMLS_ID}"

# above 1,000,000
#   1,000,0000(loan to borrower) * 0.0275(comp 2.75%) = 27,500   <-- gci 


#  27,500 * 0.2(20% goes to company) = 5,500  
# 27,500 * 0.8(80% goes to ML0) = 22,000

#   5,500(compnay makes in one loan) * 32(number of loans) = 176,000(company makes this much,cap)

#   176,000 / 0.2 = 880,000  <--- 100% commision  20 goes to company and 80 goes to MLO


# loan_amount * 0.0275 = GCI <-- company gets 20% of this much

# example loan_amount = 500,000 ,then 500,000 * 0.0275 = 13,750(gci)
# 13,750(gci) * 0.2 = 2,750   <-- comission company gets
# 
# loan amount = 400,000 * 0.0275 = 11,000(gci)
# 11,000 * 0.2 = 2,200 <- commision company get

# (5,500 + 2,570 + 2,200 )= 10,270 (total company income)? > = 176,000 ==> 100% * gci to MLO else MLO gets 0.8 * gci 

# if total_company_income < 176000(cap):
# 	then: 
# 		company_get = 20 * gci;
# 	else:
# 		company_get = 0
# 		mlo_get = 100% * gci

