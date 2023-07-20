from django import forms
from django.forms import ModelForm
from .models import complaint,accidents_reported

class complaintForm(ModelForm):
    class Meta:
        model=complaint
        fields='__all__'

        labels={
     'user_id':'User ID:',
     'city_id':'City ID',
     'area_id':'Area ID',
     'description':'Description',
    
    }
        widgets={
      'user_id':forms.Select(attrs={'class':'form-control','placeholder':'User id'}),
      'city_id':forms.Select(attrs={'class':'form-control','placeholder':'City id'}),
      'area_id':forms.Select(attrs={'class':'form-control','placeholder':'Area id'}),
      'description':forms.TextInput(attrs={'class':'form-control','placeholder':'description'}),
      
    }

class accidents_reportedForm(ModelForm):
    class Meta:
        model=accidents_reported
        fields='__all__'
    labels={
     'user_id':'User ID:',
     'area_id':'Area ID',
     'accident_type':'Accident type',
     'death_rate':'Death rate',
    
    }
    widgets={
      'user_id':forms.Select(attrs={'class':'form-control','placeholder':'User id'}),
      'accident_type':forms.Select(attrs={'class':'form-control','placeholder':'Accident Type'}),
      'area_id':forms.Select(attrs={'class':'form-control','placeholder':'Area id'}),
      'death_rate':forms.TextInput(attrs={'class':'form-control','placeholder':'death rate'}),
      
    }
  
        
    