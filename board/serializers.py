from rest_framework import serializers
from .models import Board, Task
from django.contrib.auth.models import User
from django.utils.text import slugify

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
    # class Meta:
    #     model = User
    #     fields = '__all__'
    #     extra_kwargs = {
    #         'password': {'write_only': True},
    #         'username': {'required': False},
    #     }

    # def validate_username(self, value):
    #     if ' ' in value:
    #         raise serializers.ValidationError("Username should not contain spaces.")
    #     return value

    # def create(self, validated_data):
    #     first_name = validated_data.get('first_name', '')
    #     last_name = validated_data.get('last_name', '')
    #     username = validated_data.get('username')
    #     # if not username:
    #     #     base_username = slugify(f"{first_name} {last_name}")
    #     #     username = base_username
    #     #     counter = 1
    #     #     while User.objects.filter(username=username).exists():
    #     #         username = f"{base_username}{counter}"
    #     #         counter += 1

    #     user = User(
    #         username=username,
    #         first_name=first_name,
    #         last_name=last_name,
    #         # email=validated_data.get('email', '')
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

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
        