from django.forms import ModelForm
from .models import Candidate


class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'email', 'phone', 'course', 'semester', 'analytical_history']