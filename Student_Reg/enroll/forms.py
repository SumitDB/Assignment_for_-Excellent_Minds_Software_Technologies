from django import forms
from .models import User
Citys=(("PUNE", "PUNE"),
    ("DELHI", "DELHI"),
    ("HYDRBAD", "HYDRABD"),
    ("BANGLORE", "BANGLORE"),
    ("SURAT", "SURAT"),)
Skills=(
    ("PYTHON", "PYTHON"),
    ("C", "C"),
    ("C++", "C++"),
    (".NET", ".NET"),
    ("JAVA", "JAVA"),)

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email', 'skill','city']
        widgets = {
            'skill':forms.MultipleChoiceField(choices = Skills),
            'city':forms.MultipleChoiceField(choices = Citys),            
            }




    