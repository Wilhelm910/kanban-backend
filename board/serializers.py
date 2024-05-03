from rest_framework import serializers
from .models import Board, Task
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
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            # email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        # instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
        
class BoardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Board
        fields = "__all__"
        