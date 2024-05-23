from django.db import models

class GrowthShare(models.Model):
    percentage = models.FloatField()
    amount     = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.percentage} - {self.amount}"
    
    
class HyperGrowthShare(models.Model):
    percentage = models.FloatField()
    amount     = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.percentage} - {self.amount}"
    
    
class AnnualRevenueShare(models.Model):
    percentage = models.FloatField()
    amount     = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.percentage} - {self.amount}"

class RevenueShare(models.Model):
    level                = models.IntegerField(default=1)
    growth_share         = models.ForeignKey(GrowthShare,on_delete=models.CASCADE,blank=True,null=True)
    mlos                 = models.ForeignKey('recruiter.MLO',on_delete=models.CASCADE)
    hyper_growth_share   = models.ForeignKey(HyperGrowthShare,on_delete=models.CASCADE)
    annual_revenue_share = models.ForeignKey(AnnualRevenueShare,on_delete=models.CASCADE)
    ahf_charity          = models.IntegerField(default=0)
    recruiter            = models.ForeignKey('recruiter.Recruiter',on_delete=models.CASCADE)
    
    def __str__(self):
        return f"level-{self.level} - growth share -{self.growth_share} - ahf charity{self.ahf_charity}"

    
    
    
    