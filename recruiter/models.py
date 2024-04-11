from django.db import models
from django.contrib.auth.models import User
from utils.base import BaseModelMixin
from django.contrib.auth.models import User




class MLOSAFETESTRESULT(BaseModelMixin):
    """
		MLO must take this test in order to be egible for loans and rank
    """
    
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    total = models.FloatField(blank=False,null=False)
    
    
    def __str__(self):
        if self.status == True:
            return f'MLO {self.user.username} passed test'
        else:
            return  f'MLO {self.user.username} failed test'
        
        
        
        
class NMLSPROCESSINGFEE(BaseModelMixin):
    """
		NMLS Processing fee
		
    """
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    total = models.FloatField(blank=False,null=False)
    
    def __str__(self):
        return self.total
    
    
class FBICRIMALBACKGROUNDCHECKINFO(BaseModelMixin):
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    document = models.ImageField(upload_to="/media/documents/")
    reason_for_background_check = models.TextField()
    crimal_history= models.TextField()
    
    def __str__(self) -> str:
        return self.user.username + "FBI Report"
    
    

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
	gci = models.FloatField()

	date_joined = models.DateTimeField(auto_now = True)

	# for million of dollars
	break_point  =   models.FloatField(blank = True,null=True)
	growth_share =   models.CharField(max_length = 10,choice =GROWTH_SHARE)
	hyper_growth_share =   models.CharField(max_length = 10,choice =HYPER_GROWTH_SHARE)



	def sponsor(self,sponsor_id_number):
		self.NMLS_sponsor_id = sponsor_id_number
		self.save()
		return sponsor_id_number


	def save(self):
		cap = (0.25) * (2) * (10**6)
		if self.annual_production > cap:
			pass

		self.MLO_commision = None

	def __str__(self):
		return f"{self.name}__{self.NMLS_ID}"

# above 1,000,000
#   1,000,0000 * 0.0275 = 27,500   <-- commision must company get maxmium gci 
#   27,500 * 0.2 = 5,500  
#   5,500 * 32 = 176,000
#   176,000 / 0.2 = 880,000  <--- total commision 


# loan_amount * 0.0275 = GCI <-- company gets 20% of this much
# example loan_amount = 500,000 ,then 500,000 * 0.0275 = 13,750
# 13,750 * 0.2 = 2,750   <-- comission company gets
# 
# loan amount = 400,000 * 0.0275 = 11,000
# 11,000 * 0.2 = 2,200 <- commision company get

# 5,500 + 2,570 + 2,200 = 10,270 ? > = 176,000 ==> 100% * gci to MLO else MLO gets 0.8 * gci


