from django.contrib.auth.models import AnonymousUser
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.recruiter.models import (CompPlan,Bps,LoanBreakPoint,Branch)
import numpy as np




class HomeAPIView(APIView):
    """
    A simple API view that returns a JSON response.
    """
    def get_queryset(self,*args,**kwargs):
        return CompPlan.objects.all()
    
    
    def get(self, request):
        
        data = {}
        user = request.user
        
        try:
            bps = Bps.objects.filter(user = user).first()
        except Bps.DoesNotExist as e:
            raise e
        
        try:
            loan_break_point = LoanBreakPoint.objects.filter(user = user).first()
            
        except LoanBreakPoint.DoesNotExist as e:
            raise e
        
        try:
        
            branch = Branch.objects.filter(user = user).first()
        except Branch.DoesNotExist as e:
            raise e
    

        if not isinstance(request.user, AnonymousUser):
            try:
                comp_plan = CompPlan.objects.all().filter(user = user).first()
            except CompPlan.DoesNotExist as e:
                raise e
            
            gci = bps.bps * loan_break_point.loan_break_point / 10000 + comp_plan.Flat_Fee
            bps_from_min_to_max            = []  # bps from 50 to 250
            branch_for_bps_from_min_to_max = []
            gci_for_bps_from_min_to_max    = []
            ahf_for_bps_from_min_to_max    = []
    
     
            if comp_plan != None:
                if comp_plan.Percentage == 0.0:
                    bps_from_min_to_max              = [0,0] + [num*comp_plan.Percentage for num in range(100,250,25)]+[0]
                    gci_for_bps_from_min_to_max      = [gci/(num or 1) * 10000 for num in bps_from_min_to_max] 
                    ahf_for_bps_from_min_to_max      = [(1 - branch.commission) * num for num in bps_from_min_to_max] 
                    branch_for_bps_from_min_to_max   = [branch.commission * num for num in bps_from_min_to_max]
                else:
                    bps_from_min_to_max              = [50,100] + [num for num in range(100,250,25)]+[250]
                    gci_for_bps_from_min_to_max      = [gci/(num) * 10000 for num in bps_from_min_to_max] 
                    ahf_for_bps_from_min_to_max      = [(1 - branch.commission) * num for num in bps_from_min_to_max] 
                    branch_for_bps_from_min_to_max   = [branch.commission * num for num in bps_from_min_to_max]
                    
            
                data = [
                    bps_from_min_to_max,
                    gci_for_bps_from_min_to_max,
                    branch_for_bps_from_min_to_max,
                    ahf_for_bps_from_min_to_max
                ]

                data_np = np.array(data)
                data_transposed = np.transpose(data_np)
    
            else:
                return Response({
                    'msg':f'no comp plan found for user {request.user}'
                })
            
            return Response(data_transposed)
        else:
            return Response({
                    'msg':f'no comp plan found for user {request.user}'
                })
            

    def post(self, request):
        data = request.data
        # Perform some processing on the data
        processed_data = {
            'message': 'Data processed successfully',
            'result': data
        }
        return Response(processed_data, status=201)