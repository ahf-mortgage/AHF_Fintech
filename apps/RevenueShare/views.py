from django.shortcuts import render
from .models import *

def revenue_view(request):
    context = {
        
    }
    return render(request,"home/entry.html",context)



all_revenues  = RevenueShare.objects.all()
total_all_revenue_share = 0
for revenue in all_revenues:
    total_all_revenue_share += revenue.annual_revenue_share.percentage
    

    

