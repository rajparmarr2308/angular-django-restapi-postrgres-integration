from rest_framework import serializers
from .models import Form

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model=Form
        fields=('id', 'fname', 'lname', 'email','phone','adress1','adress2','city','state','zipcode')
        
