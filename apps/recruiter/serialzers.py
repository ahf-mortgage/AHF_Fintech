from rest_framework import serializers
from .models import Edge,Node

class EdgeSerializer(serializers.ModelSerializer):
    from_ = serializers.SerializerMethodField()
    to = serializers.SerializerMethodField()
    class Meta:
        model = Edge
        fields = "from_","to"

    def get_from_(self, obj):
        return obj.source_node.mlo_agent.user.username

    def get_to(self, obj):
        return obj.target_node.mlo_agent.user.username




class NodeSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()

    class Meta:
        model = Node
        fields = "label","id"

    def get_label(self, obj):
        return obj.mlo_agent.user.username

    def get_id(self, obj):
        return obj.node_id