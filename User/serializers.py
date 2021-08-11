from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        print(validated_data)

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        Profile.objects.create(user=user).save()
        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    # profile_picture = serializers.ImageField(default='default.jpg', upload_to='pfp')
    # description = serializers.CharField(max_length=250)

    # Create a custom method field
    # current_user = serializers.SerializerMethodField('_user')

    # Use this method for the custom field
    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user

    class Meta:
        model = Profile
        fields = ('user', 'profile_picture', 'description', 'status')

    def create(self, validated_data):
        profile = Profile.objects.create(
            user=validated_data['user'],
            profile_picture=validated_data['profile_picture'],
            description=validated_data['description'],
        )

        profile.save()

        return profile

    # def update(self, instance, validated_data):
    #
    #     instance.user = validated_data['user'],
    #     instance.profile_picture = validated_data['profile_picture'],
    #     instance.description = validated_data['description']
    #
    #     instance.save()
    #
    #     return instance




