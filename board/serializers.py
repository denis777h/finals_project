from .models import Username, Public_board
from rest_framework import serializers




class SerilezUsername(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Username
        fields = ['name', 'phone',]
        


class SerilezPublic_board(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Public_board
        fields = ['title', 'date_public_boards', 'auto_public', 'content', 'interest',]
    