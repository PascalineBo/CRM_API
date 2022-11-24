
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


User = get_user_model()


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password',
                  'email', 'position', 'phone' ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        password=validated_data['password'],
                                        email=validated_data['email'],
                                        position=validated_data['position'],
                                        phone=validated_data['phone']
                                        )
        return user