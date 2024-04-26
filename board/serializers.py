from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # username = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    # class Meta:
    #     model = Task
    #     fields = '__all__'
    user_info = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'
    
    def get_user_info(self, obj):
        if obj.user: 
            return {
                'id': obj.user.id,
                'username': obj.user.username
            }
        return None  
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
