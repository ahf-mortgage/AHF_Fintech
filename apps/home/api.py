from rest_framework.views import APIView
from rest_framework.response import Response
from apps.recruiter.models import CompPlan




class HomeAPIView(APIView):
    """
    A simple API view that returns a JSON response.
    """
    def get_queryset(self,*args,**kwargs):
        return CompPlan.objects.all()
    
    
    def get(self, request):
        user = request.user
        
        data = {}
        try:
            comp_plan = CompPlan.objects.all().filter(user = user)
        except CompPlan.DoesNotExist as e:
            raise e
        
        bps_from_min_to_max           = []  # bps from 50 to 250
        branch_for_bps_from_50_to_250 = []
        gci_for_bps_from_50_to_250    = []
        ahf_for_bps_from_50_to_250    = []
        
        if comp_plan.Percentage == 0.0:
            bps_from_50_to_250            = [0,0] + [num*comp_plan.Percentage for num in range(100,250,25)]+[0]
        else:
            bps_from_50_to_250            = [50,100] + [num for num in range(100,250,25)]+[250]
        

        return Response(data)
    
    

    def post(self, request):
        data = request.data
        # Perform some processing on the data
        processed_data = {
            'message': 'Data processed successfully',
            'result': data
        }
        return Response(processed_data, status=201)