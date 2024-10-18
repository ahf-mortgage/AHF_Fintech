import requests
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect,resolve_url
from django.urls import resolve,reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from collections import deque
from django.contrib.auth.models import User
from collections import Counter
from apps.recruiter.models import (
    CompPlan,
    Bps,
    LoanBreakPoint,
    Branch,
    Edge,
    Node,
    MLO_AGENT,
    LoanAmount,
    Loan)
from apps.RevenueShare.models import AnnualRevenueShare
from utils.pagination import EdgePagination
from utils.ahf_annual_cap_data import ahf_annual_cap_data as aacd
from .serialzers import NodeSerializer,EdgeSerializer
import numpy as np
import math
from django.utils import timezone
from rest_framework import status
from rest_framework import generics
from django.conf import settings
from decouple import config
from .serialzers import LoanAmountSerializer
from .utils import calculate_commissions



data = {
    "bps_from_min_to_max": [
        50,
        100,
        100,
        125,
        150,
        175,
        200,
        225,
        250
    ],
    "gci_for_bps_from_min_to_max": [
        246913400,
        123456700,
        123456700,
        98765360,
        82304466.66666667,
        70546685.71428572,
        61728350,
        54869644.44444445,
        49382680
    ],
    "branch_for_bps_from_min_to_max": [
        49.5,
        99,
        99,
        123.75,
        148.5,
        173.25,
        198,
        222.75,
        247.5
    ],
    "ahf_for_bps_from_min_to_max ": [
        0.5,
        1,
        1,
        1.25,
        1.5,
        1.75,
        2,
        2.25,
        2.5
    ]
}

# Convert the data to a NumPy array
data_array = np.array([
    data["bps_from_min_to_max"],
    data["gci_for_bps_from_min_to_max"],
    data["branch_for_bps_from_min_to_max"],
    data["ahf_for_bps_from_min_to_max "]
]).T

# Convert the NumPy array to a list of dictionaries
rows = [
    dict(zip(data.keys(), row))
    for row in data_array
]





class RecruiterAPIView(APIView):
    """
    A simple API view that returns a JSON response.
    """
    def get_queryset(self,*args,**kwargs):
        return CompPlan.objects.all()
    
    
    def get(self, request):
        
        data = {}
        user = request.user
        
        return Response(data)
        
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
        

                data = {
                bps_from_min_to_max,
                gci_for_bps_from_min_to_max,
                branch_for_bps_from_min_to_max,
                ahf_for_bps_from_min_to_max
                }
              
                    
            else:
                return Response({
                    'msg':f'no comp plan found for user {request.user}'
                })
            
            return Response(data)
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



class CompPlanAPIView(APIView):
    """
    A simple API view that returns a JSON response.
    """
    def get_queryset(self,*args,**kwargs):
    


        return CompPlan.objects.all()


    def get(self,request,*args,**kwargs):
        user = request.user
        loan_break_point     = LoanBreakPoint.objects.filter(user = user).first()
        comp_plan_obj        = CompPlan.objects.filter(user = user).first()
        branch               = Branch.objects.filter(user = user).first()
        data = {
            "flatFee":comp_plan_obj.Flat_Fee,
            "ff1000":comp_plan_obj.FF_MIN_LOAN,
            "percentage":comp_plan_obj.Percentage,
            "max":comp_plan_obj.MAX_GCI,
            "loanBreakPoint":loan_break_point.loan_break_point,
            "split":branch.commission
        }
        return Response(data)
    

    def comp_plan_change_view(self,request):
        """
            This function handle comp plane changes
            
            Flat_Fee=max_gci*loan_below_limits[len(loan_below_limits) -1]/10000

        """
        user   = request.user
        maximumMompensation = request.data.get('maximumMompensation',None)
        maxGci              = request.data.get('maxGci',None)
        compPlan            = request.data.get('compPlan',None)
        FFMINLOAN           = request.data.get('FFMINLOAN',None)
        loanBreak           = request.data.get('loanBreak',None)
        branchAmount        = request.data.get('branchAmount',None)


        loan_break_point     = LoanBreakPoint.objects.filter(user = user).first()
        comp_plan_obj        = CompPlan.objects.filter(user = user).first()
        branch               = Branch.objects.filter(user = user).first()

        Maximum_Compensation =  maximumMompensation
        max_gci              =  maxGci  
        FF_MIN_LOAN          =  compPlan  
        comp_plan            =  FFMINLOAN
        loan_break           =  loanBreak   
        branch_amount        =  branchAmount
        
        if branch_amount != None:
            branch_amount = float(branch_amount)
            if branch_amount > 99:
                branch_amount = 99
    
        MIN_LOAN               =  100000 
        bps                    =  Bps.objects.all().first()
        rows                   = [50] +  [num for num in range(100,275,25)]
        row_counter            = [i-7 for i in range(7,7+ len(rows))]
        
        
        loan_below_limits      = [num for num in range(int(loan_break_point.loan_break_point),MIN_LOAN - MIN_LOAN,-MIN_LOAN)]  
        gci_result             = [(comp_plan_obj.Percentage * 100) * num / 10000 for num in range(int(loan_break_point.loan_break_point),MIN_LOAN - MIN_LOAN,-MIN_LOAN)]
        peak_loan_below_limits = loan_below_limits[len(loan_below_limits) - 1]
        peak_gci_results       = gci_result[len(gci_result)-1]     
        Flat_Fee               = comp_plan_obj.FF_MIN_LOAN - ((float(comp_plan) * peak_loan_below_limits)/100)
        
    

        if float(max_gci) > float(Maximum_Compensation):
            max_gci = Maximum_Compensation
                    
        if FF_MIN_LOAN != None:
            comp_plan_obj.FF_MIN_LOAN = float(FF_MIN_LOAN)
            comp_plan_obj.save()
            
        
        if branch_amount:
            comp_plan_obj.FF_MIN_LOAN           =  float(FF_MIN_LOAN)
            comp_plan_obj.MAX_GCI               =  max_gci
            comp_plan_obj.Maximum_Compensation  =  float(Maximum_Compensation)
            comp_plan_obj.Flat_Fee              =  Flat_Fee
            comp_plan_obj.Percentage            =  float(comp_plan)
            loan_break_point.loan_break_point   =  loan_break
            branch_amount                       =  int(branch_amount) / 100
            branch.commission                   =  branch_amount
            bps.bps                             =  float(comp_plan) * 100
            
            bps.save()
            loan_break_point.save()
            comp_plan_obj.save()
            branch.save()
            return Response({
                "saved":True
            })  
        return Response({
                "saved":False
            })  



    def post(self, request):
        response = self.comp_plan_change_view(request)
    
        data = request.data
    
        processed_data = {
            'message': 'Data processed successfully',
            'result': data
        }

        return response





class NodeGraphView(ListAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
 

    def get(self, request, *args, **kwargs):
    

        edges =  Edge.objects.all() # john_edges.union(ashaton3_edges)
        node_list = Node.objects.all()
        level = 1
   
        data_ = []
        nodes = []
        _edges = []
        level_source_target = {}
        level = 1
        counter  = {

        }

     
        x,y = 400,50
    
        for node in node_list:
            nodes.append({
                    "id":f"{node.pk}",
                    "x":x,
                    "y":y,
                    'name':node.mlo_agent.user.username,

                })
            x,y = x - 50,y + 100

        for edge in edges:
            _edges.append({
                "id": edge.pk,
                "from":f"{edge.source_node.pk}",
                "to":f"{edge.target_node.pk}",
                })
        

        return Response({
            'nodes':nodes,
            "edges":_edges
        })






class NodeTableView(ListAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
 

    def get(self, request, *args, **kwargs):
    

        edges =  Edge.objects.all() # john_edges.union(ashaton3_edges)

        node_list = Node.objects.all()
        level = 1
   
        data_ = []
        nodes = []
        _edges = []
        level_source_target = {}
        level = 1
        counter  = {

        }

        for node in node_list:
            nodes.append({
                "id":f"{node.pk}",
                "label":node.mlo_agent.user.username
            })

        for edge in edges:
            _edges.append({
                "id": edge.pk,
                "source": f"{edge.source_node.pk}",
                "target": f"{edge.target_node.pk}",
                "label": f'{edge.source_node.mlo_agent.user.username} sponsored {edge.target_node.mlo_agent.user.username}'
                })
        
   
        return Response({
            'parents':nodes,
            "children":_edges
        })





class EdgeGraphView(APIView):
    queryset = Edge.objects.all()
    serializer_class = EdgeSerializer

    def get(self, request, *args, **kwargs):
        edges = Edge.objects.all()
        level = 1
        data_ = []
        for obj in edges:
            data = {
               "id":obj.edge_id,
                "source":obj.source_node.mlo_agent.user.username,
                "target": obj.target_node.mlo_agent.user.username
            }
            data_.append(data)
  
            level += 1
        return Response(data_)




def calculate_commission_for_level_0(node,total_commission,split):
    mlo_agent   = node.mlo_agent
    date_joined = mlo_agent.date_joined
    now = timezone.now()
    return split* total_commission


class GetNodeInfo(APIView):
    queryset = Node.objects.all()
    def get(self, request, *args, **kwargs):
        query = request.GET
        found = False
        id = query.get('id',None)
        parent_id = query.get('parent_id',None)
        children = []
        first_node = Node.objects.all()[0]
        first_edge = Edge.objects.filter(source_node=first_node)
        try:
            node = Node.objects.filter(pk = id).first()
            parent_node = Node.objects.filter(pk = parent_id).first()
        except Node.DoesNotExist as e:
            raise e
        try:
            edges = Edge.objects.filter(source_node= node)
            for child in edges:
                children.append(child.target_node.mlo_agent.user.username)     
        except Edge.DoesNotExist as e:
            raise e
        return Response({
            'parent':parent_node.mlo_agent.user.username,
            'mlo':node.mlo_agent.user.username,
            'number_childern':len(edges),
            'children':children
        })




class GetLevelInfo(APIView):
    queryset = Node.objects.all()
    def get(self, request, *args, **kwargs):
        node_id = request.GET.get('node_id',None)
        user_id = request.GET.get('user_id',None)
        user = User.objects.filter(id = user_id).first()
        
      
        if user_id == None:
            starting_node = Node.objects.all().first()
        starting_node = Node.objects.filter(mlo_agent__user =user).first()
        loan_user  = starting_node.mlo_agent.user
        queue         = deque([(starting_node, 0)])
        node_levels   = {starting_node.mlo_agent.user.username: 0}
        data          = []
        level_to_commission = {}
        levels = [i for i in range(1,8)]

        all_revenue_shares = AnnualRevenueShare.objects.all()
        try:
            loan_break_point = LoanBreakPoint.objects.all().first()
        except LoanBreakPoint.DoesNotExist as e:
            raise e
 
            
        try:
            comp_plan        = CompPlan.objects.all().first()
        except CompPlan.DoesNotExist as e:
            raise e

        try:
            bps        = Bps.objects.all().first()
        except Bps.DoesNotExist as e:
            raise e
        

        annual_revenue_shares = []
        test_branch_gross_income  =  aacd.get("test_branch_gross_income",None)
        ahf_amount                =  aacd.get("ahf_amount",1)
        AD9                       =  math.ceil(float(test_branch_gross_income)/float(ahf_amount) * 100)
        split                     = Branch.objects.filter().first().commission
        gci                       =   (comp_plan.Percentage * 100) * loan_break_point.loan_break_point/10000  + comp_plan.Flat_Fee
        index = 0


        calculate_commissions(levels, all_revenue_shares, starting_node, AD9, split)


        for level,AD12 in zip(levels,annual_revenue_shares):
            level_to_commission[0] =  calculate_commission_for_level_0(starting_node,AD9,split)
            AE12 = AD9*AD12
          
            AG12 = AE12/2
            level_to_commission[level] = AG12

        while queue:
            node, level = queue.popleft()
            for edge in node.outgoing_edges.all():
                target_node = edge.target_node
                if target_node not in node_levels:
                    node_levels[target_node.mlo_agent.user.username] = level + 1
                    queue.append((target_node, level + 1))


        for mlo in node_levels:
            agent = MLO_AGENT.objects.filter(user__username = mlo).first()
            node = Node.objects.filter(mlo_agent = agent).first()
            edge = Edge.objects.filter(source_node= node)
            loan      = agent.loan 


            print("out going edge number = ",len(edge.target_node.all()))
          
           
  
            _data = {
                'mlo':mlo,
                'level':node_levels.get(mlo,None),
                'commission': f"{math.ceil(level_to_commission.get(node_levels.get(mlo,None),0)):,}",
                'loan': len(loan.amount.all()) if loan  != None  else 0,
                'total_amount':f"{math.ceil(sum([amount.loan_amount if loan != None else 0 for amount in loan.amount.all()])):,}",
                "split":f"{split * 100}%",
                'file_reference':loan.File_reference,
                'loan_amount':loan.amount.all().first().loan_amount,
                'date_funded':loan.amount.all().first().loan_date,
                'gci':f"$ {gci:,}",
                'bps':loan.bps,
                'ahf_commission':f"{float(1 - split) * float(gci):,}",
                'branch_commission':float(split) * float(gci)
            }

            data.append(_data)
        return Response(data)



class LoanDetailView(APIView):
    queryset        = Node.objects.all()
    def get(self, request, *args, **kwargs):
        loan_detail = request.GET.get('loan_detail',None)
        id          = loan_detail
        node_level  =  request.GET.get("level",None)
        user        = User.objects.filter(id = id).first()
        print("user = ",user)
        mlo         = MLO_AGENT.objects.filter(user = user).first()
        node        = Node.objects.filter(mlo_agent = mlo).first()
        edge        = Edge.objects.filter(source_node =node ).first()
        loan        = mlo.loan 
    

        amounts     = loan.amount.all()

        all_revenue_shares = AnnualRevenueShare.objects.all().reverse()
        try:
            loan_break_point = LoanBreakPoint.objects.filter(user = request.user).first()
        except LoanBreakPoint.DoesNotExist as e:
            raise e
            
        try:
            comp_plan  = CompPlan.objects.filter(user = request.user).first()
        except CompPlan.DoesNotExist as e:
            raise e

        try:
            bps = Bps.objects.filter(user = request.user).first()
        except Bps.DoesNotExist as e:
            raise e
        

    
        test_branch_gross_income  =  aacd(request).get("test_branch_gross_income",None)
        ahf_amount                =  aacd(request).get("ahf_amount",1)
        AD9                       =  math.ceil(float(test_branch_gross_income)/float(ahf_amount) * 100)
        split                     =  Branch.objects.filter(user = request.user).first().commission
   

        data = []
        innner_outgoing_edges = None
        MIN_LOAN = 100000 
        total_commission = 0
        total_ahf_commission = 0
        total_mlo = 0

        test_branch_gross_income  =  aacd(request).get("test_branch_gross_income",None)
        ahf_amount                =  aacd(request).get("ahf_amount",1)
        AD9                       =  math.ceil(float(test_branch_gross_income)/float(ahf_amount) * 100)
        split                     =  Branch.objects.filter(user = request.user).first().commission
        gci                       =  (comp_plan.Percentage * 100) * loan_break_point.loan_break_point/10000  + comp_plan.Flat_Fee
        index = 1
        level_to_commission = {}
        levels = [i for i in range(1,8)]
     
        starting_node =node
    
        # n= {0: Decimal('41800.00'), 1: 457.1875, 2: 522.5}
        # evel_to_commission= {0: Decimal('22000.00'), 1: 240.625, 2: 275.0}

        # level to recruiter comission
        for level,AD in zip(levels,all_revenue_shares):

            level_to_commission[0] =  calculate_commission_for_level_0(starting_node,AD9,split)
            AE = AD9 * AD.percentage / 100
            AG = AE
         
            level_to_commission[level] = AG/2


        outgoing_edges = node.outgoing_edges.all()
        total_number_of_agent_level_2 = 0
        recruiter_commission = 0
        for oe in outgoing_edges:
            innner_outgoing_edges = oe.source_node.outgoing_edges.all()
            total_number_of_agent_level_2 += len(innner_outgoing_edges) 

        total_number_of_sponsored_agents = len(outgoing_edges)
        

        for level in range(1,len(node_level) + 1):
            if level == 1:
                recruiter_commission += math.ceil(level_to_commission.get(level,0))  * total_number_of_sponsored_agents 
            elif level == 2:
                recruiter_commission += math.ceil(level_to_commission.get(level,0))  * total_number_of_agent_level_2 
            else:
                recruiter_commission = 0


        parents = {}
        for edge in Edge.objects.all():
            parents[f"parent_of_{edge.target_node.mlo_agent.user.username}"] = edge.source_node.mlo_agent.user.username
        
     
        for amount in amounts:
            gci = float(comp_plan.Percentage * 100) * float(amount.loan_amount/10000)  + comp_plan.Flat_Fee
            total_commission += float(1-split) * float(gci) 
            total_ahf_commission += float(split) * float(gci)
            _data = [
               
                f"{math.ceil(split * 100)}%",
                amount.File_reference,
                f"${math.ceil(amount.loan_amount):,}",
                amount.loan_date,
                f"${math.ceil(gci):,}",
                loan.bps,
                f"${math.ceil(float(1-split) * float(gci)):,}" , 
                f"${math.ceil(float(split) * float(gci)):,}",
                recruiter_commission
                  
            ]
            total_mlo += 1
            index += 1
            data.append(_data)
            data.append({"mlo":mlo.user.username})
        data.append({'total_mlo':total_mlo})
        return Response(data)




class GetMloLevelInfo(APIView):
    queryset = Node.objects.all()
    def get(self, request, *args, **kwargs):
        mlo_id = request.GET.get('mlo_id',None)
        mlo = MLO_AGENT.objects.filter(id =mlo_id).first()

        user          = request.user
        request_mlo   = MLO_AGENT.objects.filter(user = user).first()
        request_agent = Node.objects.filter(mlo_agent= request_mlo).first()
        starting_node = request_agent
        queue         = deque([(starting_node, 0)])
        node_levels   = {starting_node.mlo_agent.user.username: 0}

        while queue:
            node, level = queue.popleft()
            for edge in node.outgoing_edges.all():
                target_node = edge.target_node
                if target_node not in node_levels:
                    node_levels[target_node.mlo_agent.user.username] = level + 1
                    queue.append((target_node, level + 1))
    
        return Response({
            'level':node_levels.get(mlo.user.username)
        })





class GetAllNodes(APIView):
    def get_queryset(self):
        return Node.objects.all()
    
    def get(self, request, *args, **kwargs):

        edge_id = request.GET.get("q")
        if edge_id:
            edge = Edge.objects.filter(edge_id = edge_id)
            edge.delete()

        nodes = self.get_queryset()
        edges = Edge.objects.all()
        all_target_nodes = []

        for edge in edges:
            all_target_nodes.append(edge.target_node)
        eligible_nodes = [item for item in nodes if item not in all_target_nodes]
    
        serializer = NodeSerializer(eligible_nodes[1::], many=True)  # Serialize the nodes
        return Response(serializer.data, status=status.HTTP_200_OK) 
    

    def post(self, request, *args, **kwargs):
        data = request.data
        source_node_mlo = data.get('source_node',"")
        target_node_mlo = data.get('target_node',"")
        source_node = Node.objects.filter(mlo_agent__user__username = source_node_mlo).first()
        target_node = Node.objects.filter(mlo_agent__user__username = target_node_mlo).first()
        last_edge_id = Edge.objects.all().last().edge_id
        new_edge = Edge.objects.create(edge_id = last_edge_id + 1,source_node = source_node,target_node = target_node)
        print("new edge = ",new_edge)
 
        return Response({"node_id":source_node.node_id}, status=status.HTTP_200_OK) 
    



def single_mlo_info(request,node_id):
        node_id = request.GET.get('node_id',None)
      
        
      
        if node_id == None:
            starting_node = Node.objects.filter(node_id=node_id).first()
        starting_node = Node.objects.all().last()
        loan_user  = starting_node.mlo_agent.user
        queue         = deque([(starting_node, 0)])
        node_levels   = {starting_node.mlo_agent.user.username: 0}
        data          = []
        level_to_commission = {}
        levels = [i for i in range(1,8)]

        all_revenue_shares = AnnualRevenueShare.objects.all()
        try:
            loan_break_point = LoanBreakPoint.objects.all().first()
        except LoanBreakPoint.DoesNotExist as e:
            raise e
 
            
        try:
            comp_plan        = CompPlan.objects.all().first()
        except CompPlan.DoesNotExist as e:
            raise e

        try:
            bps        = Bps.objects.all().first()
        except Bps.DoesNotExist as e:
            raise e
        

        annual_revenue_shares = []
        test_branch_gross_income  =  aacd.get("test_branch_gross_income",None)
        ahf_amount                =  aacd.get("ahf_amount",1)
        AD9                       =   math.ceil(float(test_branch_gross_income)/float(ahf_amount) * 100)
        split                     =   Branch.objects.filter().first().commission
        gci                       =   (comp_plan.Percentage * 100) * loan_break_point.loan_break_point/10000  + comp_plan.Flat_Fee
        index = 0

 

        for level,AD12 in zip(levels,annual_revenue_shares):
            level_to_commission[0] =  calculate_commission_for_level_0(starting_node,AD9,split)
            AE12 = AD9*AD12
          
            AG12 = AE12/2
            level_to_commission[level] = AG12

        while queue:
            node, level = queue.popleft()
            for edge in node.outgoing_edges.all():
                target_node = edge.target_node
                if target_node not in node_levels:
                    node_levels[target_node.mlo_agent.user.username] = level + 1
                    queue.append((target_node, level + 1))


        for mlo in node_levels:
            mlo_agent = MLO_AGENT.objects.filter(user__username = "tinsae").first()
            user      = User.objects.filter(username = mlo).first()
            mlo_agent = MLO_AGENT.objects.filter(user=user).first()
            loan      = Loan.objects.filter(mlo_agent__user__username = loan_user).first()
          
           
  
            _data = {
                'mlo':mlo,
                'level':node_levels.get(mlo,None),
                'commission': f"{math.ceil(level_to_commission.get(node_levels.get(mlo,None),0)):,}",
                'loan': len(loan.amount.all()) if loan  != None  else 0,
                'total_amount':f"{math.ceil(sum([amount.loan_amount if loan != None else 0 for amount in loan.amount.all()])):,}",
                "split":f"{split * 100}%",
                'file_reference':loan.File_reference,
                'loan_amount':loan.amount.all().first().loan_amount,
                'date_funded':loan.amount.all().first().loan_date,
                'gci':f"$ {gci:,}",
                'bps':loan.bps,
                'ahf_commission':f"{float(1 - split) * float(gci):,}",
                'branch_commission':float(split) * float(gci)
            }

            data.append(_data)
        return data
     
class ChartView(APIView):    
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get("user_id",None)
        current_mlo = None
        current_node = None
        data = []
        all_edges = Edge.objects.all()
    
     

        try:
            user = User.objects.filter(id = user_id).first()
            current_mlo = user.user_mlo.all().first()
            current_node = Node.objects.filter(mlo_agent = current_mlo).first()
        except User.DoesNotExist as e:
            print("e")



        if current_mlo:
            starting_node = Edge.objects.filter(source_node__mlo_agent= current_mlo).first()
        else:
            return redirect(resolve("/error/"))
            print("Empty Screen")
        BASE_URL = config("BASE_URL")
    
  
        if current_mlo and starting_node:
            data.append({
                "id":starting_node.source_node.mlo_agent.user.id,
                "name":starting_node.source_node.mlo_agent.user.username
            })


            outgoing_edges = current_node.outgoing_edges.all()
            print("user = ",user.is_superuser)
            if user and user.is_superuser:
                outgoing_edges = Edge.objects.all()

            for edge in outgoing_edges:
                # _data = requests.get(f"{BASE_URL}/api/get_node_detail/?username={edge.target_node.mlo_agent.user.username}").json()
            
                node = {
                    "NMLS_ID":edge.target_node.mlo_agent.NMLS_ID,
                    "id":edge.target_node.mlo_agent.user.id,
                    "name":edge.target_node.mlo_agent.user.username,
                    'pid':edge.source_node.mlo_agent.user.id,
                    # "Total number of loans":_data.get("total_number_of_loans",None),
                    # "BPS":_data.get("bps",None),
                    # "Total Loan Amounts":_data.get("total_loan_amounts",None),
                    # "Split":_data.get("split",None),
                    "img":"https://www.ahf.mortgage/media/agent_placeholder.jpg"
                }
                data.append(node)
            

            return Response(data,status=status.HTTP_200_OK)
        else:
            print("redirect page =++++++++++++++++++++==")
            return Response([],status=status.HTTP_200_OK)
        


class NodeLoanDetailView(APIView):    
    def get(self, request, *args, **kwargs):
        data = []
        username = request.GET.get("username",None) 
        loan = Loan.objects.filter(mlo_agent__user__username=username).first()
        loan_amounts = loan.amount.all()
        total_loan_amount = 0
        for amount in loan_amounts:
            total_loan_amount+= amount.loan_amount


        branch = 0
        split = 0


        try:
            branch  = Branch.objects.all().first().commission
        except Branch.DoesNotExist as e:
            raise e
     
     
       

        raw_data = {
            "total_number_of_loans":len(loan.amount.all()),
            "total_loan_amounts":total_loan_amount,
            "bps":loan.bps,
            "split":branch * 100
        
        }

        return Response(raw_data)


        
class LoanAmountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoanAmount.objects.all()
    serializer_class = LoanAmountSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)