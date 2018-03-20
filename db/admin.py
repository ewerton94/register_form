from django.contrib import admin
from .models import Candidate
from .actions import export_as_csv_action

class CandidateAdmin(admin.ModelAdmin):
	list_display = ['name','course']
	actions = [export_as_csv_action("CSV Export", fields=['name','email', 'phone', 'course', 'semester', 'analytical_history'])]

admin.site.register(Candidate, CandidateAdmin)